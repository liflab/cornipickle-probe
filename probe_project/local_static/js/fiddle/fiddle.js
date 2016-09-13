var open = false;

var ListOfEditors = {};

var Grammar = {};

var CodeMirrorEditor = function(id) {
    this.m_editor = null;

    this.m_id = id;

    this.m_ruletoolbar = null;

    this.insertion = function(element) {
        this.m_editor = CodeMirror.fromTextArea(element,{
            lineNumbers:true,
            mode: "cornipickle",
            lineWrapping:true,
            theme: "none"
            // Nous devons Creer le highlight de Cornipickle et le mettre ici
            // Nous devons télécharger notre propre codemirroir
        });

        if(this.m_editor.getDoc().getValue() === "") {
            this.m_editor.setOption("theme","rubyblue");
            $("#codeMirrorInstance"+this.m_id).find(".cornipicklebutton").addClass("active");
            var scroller = this.m_editor.getScrollerElement();
            var elem = document.createElement("a");
            this.m_editor.getDoc().replaceRange("<S>\n.",{line:0,ch:0},{line:0,ch:0});
            var pos = this.m_editor.charCoords({line: 0, ch: 0}, "local");
            var endPos = this.m_editor.charCoords({line:0,ch:2},"local");
            elem.setAttribute("class", "startingrule rulebutton");
            elem.setAttribute("style", "top:" + pos.top + "px;left:" + pos.left + "px;width:" + (endPos.right-pos.left) +
                "px;height:20px;");
            elem.setAttribute("token","<S>");
            elem.setAttribute("editorid",this.m_id);
            elem.setAttribute("linecoord",0);
            elem.setAttribute("chcoord",0);
            elem.setAttribute("linecoordend",0);
            elem.setAttribute("chcoordend",2);
            $(scroller).find(".CodeMirror-sizer").append(elem);
        }
        else {
            this.m_editor.setOption("theme","hopscotch");
            $("#codeMirrorInstance"+this.m_id).find(".rawbutton").addClass("active");
        }
        this.m_editor.on("change", this.onChange);
        this.m_ruletoolbar = $("#codeMirrorInstance"+this.m_id).find(".ruletoolbar");
        this.m_ruletoolbar.attr("editorid",this.m_id);
    };

    this.displayRuleToolbar = function(button) {
        this.m_ruletoolbar.attr("token",button.attr("token"));
        if(button.attr("token") === "<var_name>" ||
            button.attr("token") === "<css_sel_part>" ||
            button.attr("token") === "<number>" ||
            button.attr("token") === "<string>" ||
            button.attr("token") === "<def_set_name>" ||
            button.attr("token") === "<pred_pattern>") {
            this.m_ruletoolbar.find(".labelterminal").append(Grammar[button.attr("token")]);
            this.m_ruletoolbar.find(".nonterminal").css("display","none");
            this.m_ruletoolbar.find(".terminal").css("display","block");
        }
        else {
            var righthand = Grammar[button.attr("token")];
            for(i = 0; i < righthand.length; i++) {
                var righthandstring = righthand[i].substring(1,righthand[i].length-1);
                this.m_ruletoolbar.find(".options").append("<option value=\""+righthandstring+"\">"+righthandstring+"</option>");
            }
            this.m_ruletoolbar.find(".terminal").css("display","none");
            this.m_ruletoolbar.find(".nonterminal").css("display","block");
        }
        this.m_ruletoolbar.attr("linecoord",button.attr("linecoord"));
        this.m_ruletoolbar.attr("chcoord",button.attr("chcoord"));
        this.m_ruletoolbar.attr("linecoordend",button.attr("linecoordend"));
        this.m_ruletoolbar.attr("chcoordend",button.attr("chcoordend"));
        this.m_ruletoolbar.css("display","block");
    };

    this.clearRuleToolbar = function() {
        this.m_ruletoolbar.css("display","none");
        this.m_ruletoolbar.find(".options").empty();
        this.m_ruletoolbar.find(".labelterminal").html("Regex: ");
        this.m_ruletoolbar.find(".terminaltextarea").val("");
        this.m_ruletoolbar.attr("token","");
    };

    this.onChange = function(codemirror, obj) {
        console.log("EVENT");
    };

    this.ruleClicked = function(button) {
        this.clearRuleToolbar();
        this.displayRuleToolbar(button);
    };

    this.terminalButtonClicked = function(button) {
        var value = this.m_ruletoolbar.find(".terminaltextarea").val();
        this.m_editor.getDoc().replaceRange(value,{line:parseInt(this.m_ruletoolbar.attr("linecoord")),
            ch:parseInt(this.m_ruletoolbar.attr("chcoord"))},{line:parseInt(this.m_ruletoolbar.attr("linecoordend")),
            ch:parseInt(this.m_ruletoolbar.attr("chcoordend"))+1});
        this.updateRuleButtons();
        this.clearRuleToolbar();
    };

    this.nonTerminalButtonClicked = function(button) {
        var rulename = this.m_ruletoolbar.find(".options").val();
        rulename = "<" + rulename + ">";
        var rule = Grammar[rulename];
        if(rule.length > 1) {
            this.m_editor.getDoc().replaceRange(rulename,{line:parseInt(this.m_ruletoolbar.attr("linecoord")),
                ch:parseInt(this.m_ruletoolbar.attr("chcoord"))},{line:parseInt(this.m_ruletoolbar.attr("linecoordend")),
                ch:parseInt(this.m_ruletoolbar.attr("chcoordend"))+1});
        }
        else {
            var content = this.m_editor.getDoc().getValue();
            var openparindex = rule[0].indexOf("(");
            if(openparindex !== -1) {
                var endparindex = rule[0].indexOf(")");
                rule[0] = rule[0].slice(0,openparindex+1) + "\n\t" + rule[0].slice(openparindex+2,endparindex-1) + "\n" +
                        rule[0].slice(endparindex,endparindex+1);
            }
            var startIndex = parseInt(this.m_editor.getDoc().indexFromPos({line:parseInt(this.m_ruletoolbar.attr("linecoord")),
                ch:parseInt(this.m_ruletoolbar.attr("chcoord"))}));
            var endIndex = parseInt(this.m_editor.getDoc().indexFromPos({line:parseInt(this.m_ruletoolbar.attr("linecoordend")),
                ch:parseInt(this.m_ruletoolbar.attr("chcoordend"))}));
            content = content.substring(0,startIndex) + rule[0] + content.substring(endIndex+1,content.length);
            this.m_editor.getDoc().setValue(content);
        }
        this.updateRuleButtons();
        this.clearRuleToolbar();
    };

    this.updateRuleButtons = function() {
        var scroller = this.m_editor.getScrollerElement();
        $(scroller).find(".CodeMirror-sizer").find(".rulebutton").remove();
        var content = this.m_editor.getDoc().getValue();
        for(i=0;content.indexOf("<",i) !== -1;) {
            var start = content.indexOf("<",i);
            var pos = this.m_editor.getDoc().posFromIndex(start);
            i = start + 1;
            var end = content.indexOf(">",i);
            var endpos = this.m_editor.getDoc().posFromIndex(end);
            var token = content.substring(start+1,end);
            this.createRuleButton($(scroller).find(".CodeMirror-sizer"),token,pos,endpos);
        }
    };

    this.createRuleButton = function(sizer,token,posStart,posEnd) {
        var startCoords = this.m_editor.charCoords(posStart,"local");
        var endCoords = this.m_editor.charCoords(posEnd,"local");

        var elem = document.createElement("a");
        elem.setAttribute("class",  token + " rulebutton");
        elem.setAttribute("style", "top:" + startCoords.top + "px;left:" + startCoords.left + "px;width:" +
            (endCoords.right-startCoords.left) + "px;height:20px;");
        elem.setAttribute("token", "<"+token+">");
        elem.setAttribute("editorid",this.m_id);
        elem.setAttribute("linecoord",posStart.line);
        elem.setAttribute("chcoord",posStart.ch);
        elem.setAttribute("linecoordend",posEnd.line);
        elem.setAttribute("chcoordend",posEnd.ch);
        sizer.append(elem);
    };
};

$('body').on('click', ".editorYellowButton", function() {
    if(!open) {
        $(".glyphicon-chevron-up").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down")
        $('.editorDropup').animate({
            top: '-=' + $('.editorPropertyMetadata').height() + 'px'
        }, 300, function() {
            open = true;
        });
    }
    else {
        $(".glyphicon-chevron-down").removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up")
        $('.editorDropup').animate({
            top: '+=' + $('.editorPropertyMetadata').height() + 'px'
        }, 300, function() {
            open = false;
        });
    }
});

$("body").on("click", ".rulebutton", function() {
    var ed = ListOfEditors[$(this).attr("editorid")];
    ed.ruleClicked($(this));
});

$("body").on("click", ".submitterminalbutton", function() {
    var ed = ListOfEditors[$(this).closest(".ruletoolbar").attr("editorid")];
    ed.terminalButtonClicked($(this));
});

$("body").on("click", ".submitnonterminalbutton", function() {
    var ed = ListOfEditors[$(this).closest(".ruletoolbar").attr("editorid")];
    ed.nonTerminalButtonClicked($(this));
});

window.onload = function() {
    $(".fiddleEditor").each( function () {
        var count = 0;
        var t = $(this)[0];
        var text = t.firstElementChild.value;
        var id = t.firstElementChild.id;
        var name = t.firstElementChild.getAttribute("name");

        $.ajax({
            url: "http://localhost:8000/fiddle/fiddleeditor",
            type: "POST",
            data: {"text":text, "id":id, "name":name},
            success: function(html) {
                var h = document.createElement("div");
                h.id = "codeMirrorInstance" + count; // Je donne ici un Id a un nouvelle élément
                h.innerHTML = html;
                t.firstElementChild.parentNode.replaceChild(h,t.firstElementChild);
                var selector = "#" + id;
                var newEditor = new CodeMirrorEditor(count);
                newEditor.insertion($(selector)[0]);

                $(".rawbutton").click(function () {
                    newEditor.m_editor.setOption("theme","hopscotch");
                    $(this).addClass("active");
                    $(this).parent().children(".cornipicklebutton").removeClass("active");
                });

                $(".cornipicklebutton").click(function () {
                    newEditor.m_editor.setOption("theme","rubyblue");
                    $(this).addClass("active");
                    $(this).parent().children(".rawbutton").removeClass("active");

                });
                ListOfEditors[count] = newEditor;
                count++;
            }
        });
    });

    $.ajax({
        url: "http://localhost:8000/fiddle/getgrammar",
        type: "POST",
        data: {"action":"getgrammar"},
        success: function(response) {
            Grammar = response;
        }
    });
};

