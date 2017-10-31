{% load staticfiles %}

require.config({
    packages: [{
        name: "codemirror",
        location: "/static/bower_components/codemirror",
        main: "lib/codemirror"
    }]
});

//Require JS
require(["codemirror"],function (CodeMirror) {
    var open = false;

    var ListOfEditors = [];

    var Grammar = {};

    var Stylesheets = {"codeMirrorBase": false,
        "corniColors": false,
        "fiddle": false,
        "theme": false}


    var CodeMirrorEditor = function (id,selectorid) {
        this.m_editor = null;

        this.m_id = id;

        this.m_ruletoolbar = null;

        this.m_selectorid = selectorid;

        this.insertion = function (element) {
            this.m_editor = CodeMirror.fromTextArea(element, {
                lineNumbers: true,
                mode: "cornipickleSimple",
                lineWrapping: true
            });

            if (this.m_editor.getDoc().getValue() === "") {
                this.m_editor.setOption("theme", "rubyblue default");
                this.m_editor.doc.cantEdit = true;
                $("#codeMirrorInstance" + this.m_id).find(".cornipicklebutton").addClass("active");
                this.m_editor.getDoc().replaceRange("<S>\n.", {line: 0, ch: 0}, {line: 0, ch: 0});
                this.createRuleButton($(this.m_editor.getScrollerElement()).find(".CodeMirror-sizer"), "S", {
                        line: 0,
                        ch: 0
                    },
                    {line: 0, ch: 2});
            }
            else {
                this.m_editor.setOption("theme", "default");
                this.m_editor.doc.cantEdit = false;
                $("#codeMirrorInstance" + this.m_id).find(".rawbutton").addClass("active");
            }
            this.m_editor.on("change", this.onChange);
            this.m_ruletoolbar = $("#codeMirrorInstance" + this.m_id).find(".ruletoolbar");
            this.m_ruletoolbar.attr("editorid", this.m_id);
        };

        this.displayRuleToolbar = function (button) {
            var token = button.attr("token");
            this.m_ruletoolbar.attr("token", token);
            this.m_ruletoolbar.find(".toolbarlabel").html(token.substring(1, token.length - 1));
            if (button.attr("token") === "<var_name>" ||
                button.attr("token") === "<css_sel_part>" ||
                button.attr("token") === "<number>" ||
                button.attr("token") === "<string>" ||
                button.attr("token") === "<def_set_name>" ||
                button.attr("token") === "<pred_pattern>") {
                this.m_ruletoolbar.find(".labelterminal").append(Grammar[button.attr("token")]);
                this.m_ruletoolbar.find(".nonterminal").css("display", "none");
                this.m_ruletoolbar.find(".terminal").css("display", "block");
            }
            else {
                var righthand = Grammar[button.attr("token")];
                for (i = 0; i < righthand.length; i++) {
                    var righthandstring = righthand[i].replace(new RegExp("<", "g"), "&lt;").replace(new RegExp(">", "g"), '&gt;');
                    this.m_ruletoolbar.find(".options").append("<option value=\"" + righthandstring + "\">" + righthandstring + "</option>");
                }
                this.m_ruletoolbar.find(".terminal").css("display", "none");
                this.m_ruletoolbar.find(".nonterminal").css("display", "block");
            }
            this.m_ruletoolbar.attr("linecoord", button.attr("linecoord"));
            this.m_ruletoolbar.attr("chcoord", button.attr("chcoord"));
            this.m_ruletoolbar.attr("linecoordend", button.attr("linecoordend"));
            this.m_ruletoolbar.attr("chcoordend", button.attr("chcoordend"));
            this.m_ruletoolbar.css("display", "block");
        };

        this.clearRuleToolbar = function () {
            this.m_ruletoolbar.css("display", "none");
            this.m_ruletoolbar.find(".options").empty();
            this.m_ruletoolbar.find(".labelterminal").html("Regex: ");
            this.m_ruletoolbar.find(".terminaltextarea").val("");
            this.m_ruletoolbar.attr("token", "");
        };

        this.onChange = function (codemirror, obj) {

        };

        this.ruleClicked = function (button) {
            this.clearRuleToolbar();
            this.displayRuleToolbar(button);
        };

        this.terminalButtonClicked = function (button) {
            var value = this.m_ruletoolbar.find(".terminaltextarea").val();
            this.m_editor.getDoc().replaceRange(value, {
                line: parseInt(this.m_ruletoolbar.attr("linecoord")),
                ch: parseInt(this.m_ruletoolbar.attr("chcoord"))
            }, {
                line: parseInt(this.m_ruletoolbar.attr("linecoordend")),
                ch: parseInt(this.m_ruletoolbar.attr("chcoordend")) + 1
            });
            this.updateRuleButtons();
            this.clearRuleToolbar();
        };

        this.nonTerminalButtonClicked = function (button) {
            var rulename = this.m_ruletoolbar.find(".options").val();
            var rule = Grammar[rulename];
            if (rule.length > 1) {
                this.m_editor.getDoc().replaceRange(rulename, {
                    line: parseInt(this.m_ruletoolbar.attr("linecoord")),
                    ch: parseInt(this.m_ruletoolbar.attr("chcoord"))
                }, {
                    line: parseInt(this.m_ruletoolbar.attr("linecoordend")),
                    ch: parseInt(this.m_ruletoolbar.attr("chcoordend")) + 1
                });
            }
            else {
                var content = this.m_editor.getDoc().getValue();
                var openparindex = rule[0].indexOf("(");
                if (openparindex !== -1 && rulename !== "<css_selector>" && rulename !== "<add>" && rulename !== "<sub>" &&
                    rulename !== "<mult>" && rulename !== "<div>") {
                    var endparindex = rule[0].indexOf(")");
                    rule[0] = rule[0].slice(0, openparindex + 1) + "\n" + rule[0].slice(openparindex + 2, endparindex - 1) + "\n" +
                        rule[0].slice(endparindex, endparindex + 1);
                }
                var startIndex = parseInt(this.m_editor.getDoc().indexFromPos({
                    line: parseInt(this.m_ruletoolbar.attr("linecoord")),
                    ch: parseInt(this.m_ruletoolbar.attr("chcoord"))
                }));
                var endIndex = parseInt(this.m_editor.getDoc().indexFromPos({
                    line: parseInt(this.m_ruletoolbar.attr("linecoordend")),
                    ch: parseInt(this.m_ruletoolbar.attr("chcoordend"))
                }));
                content = content.substring(0, startIndex) + rule[0] + content.substring(endIndex + 1, content.length);
                this.m_editor.getDoc().setValue(content);
            }
            this.updateRuleButtons();
            this.clearRuleToolbar();
        };

        this.updateRuleButtons = function () {
            var scroller = this.m_editor.getScrollerElement();
            $(scroller).find(".CodeMirror-sizer").find(".rulebutton").remove();
            var content = this.m_editor.getDoc().getValue();
            for (i = 0; content.indexOf("<", i) !== -1;) {
                var start = content.indexOf("<", i);
                var pos = this.m_editor.getDoc().posFromIndex(start);
                i = start + 1;
                var end = content.indexOf(">", i);
                var endpos = this.m_editor.getDoc().posFromIndex(end);
                var token = content.substring(start + 1, end);
                this.createRuleButton($(scroller).find(".CodeMirror-sizer"), token, pos, endpos);
            }
        };

        this.createRuleButton = function (sizer, token, posStart, posEnd) {
            var startCoords = this.m_editor.charCoords(posStart, "local");
            var endCoords = this.m_editor.charCoords(posEnd, "local");

            var elem = document.createElement("a");
            elem.setAttribute("class", "rulebutton");
            elem.setAttribute("style", "top:" + startCoords.top + "px;left:" + startCoords.left + "px;width:" +
                (endCoords.right - startCoords.left) + "px;height:25px;");
            elem.setAttribute("token", "<" + token + ">");
            elem.setAttribute("editorid", this.m_id);
            elem.setAttribute("linecoord", posStart.line);
            elem.setAttribute("chcoord", posStart.ch);
            elem.setAttribute("linecoordend", posEnd.line);
            elem.setAttribute("chcoordend", posEnd.ch);
            elem.innerHTML = token;
            sizer.append(elem);
        };
    };

    $('body').on('click', ".editorYellowButton", function () {
        if (!open) {
            $(".glyphicon-chevron-up").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down")
            $('.editorDropup').animate({
                top: '-=' + $('.editorPropertyMetadata').height() + 'px'
            }, 300, function () {
                open = true;
            });
        }
        else {
            $(".glyphicon-chevron-down").removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up")
            $('.editorDropup').animate({
                top: '+=' + $('.editorPropertyMetadata').height() + 'px'
            }, 300, function () {
                open = false;
            });
        }
    });

    $("body").on("click", ".rulebutton", function () {
        var ed = ListOfEditors[parseInt($(this).attr("editorid"))];
        ed.ruleClicked($(this));
    });

    $("body").on("click", ".submitterminalbutton", function () {
        var ed = ListOfEditors[parseInt($(this).closest(".ruletoolbar").attr("editorid"))];
        ed.terminalButtonClicked($(this));
    });

    $("body").on("click", ".submitnonterminalbutton", function () {
        var ed = ListOfEditors[parseInt($(this).closest(".ruletoolbar").attr("editorid"))];
        ed.nonTerminalButtonClicked($(this));
    });

    var codeMirrorBaseCSSLoaded = function() {
        console.log("codemirrorbasecssloaded");
        Stylesheets["codeMirrorBase"] = true;
        if(Stylesheets["codeMirrorBase"] && Stylesheets["theme"] && Stylesheets["corniColors"] && Stylesheets["fiddle"]) {
            for(var i = 0; i < ListOfEditors.length; i++) {
                allCSSLoaded(ListOfEditors[i]);
            }
        }
    };

    var fiddleCSSLoaded = function() {
        console.log("fiddleloaded");
        Stylesheets["fiddle"] = true;
        if(Stylesheets["codeMirrorBase"] && Stylesheets["theme"] && Stylesheets["corniColors"] && Stylesheets["fiddle"]) {
            for(var i = 0; i < ListOfEditors.length; i++) {
                allCSSLoaded(ListOfEditors[i]);
            }
        }
    };

    var themeCSSLoaded = function() {
        console.log("themeloaded");
        Stylesheets["theme"] = true;
        if(Stylesheets["codeMirrorBase"] && Stylesheets["theme"] && Stylesheets["corniColors"] && Stylesheets["fiddle"]) {
            for(var i = 0; i < ListOfEditors.length; i++) {
                allCSSLoaded(ListOfEditors[i]);
            }
        }
    };

    var corniColorsCSSLoaded = function() {
        console.log("cornicolorsloaded");
        Stylesheets["corniColors"] = true;
        if(Stylesheets["codeMirrorBase"] && Stylesheets["theme"] && Stylesheets["corniColors"] && Stylesheets["fiddle"]) {
            for(var i = 0; i < ListOfEditors.length; i++) {
                allCSSLoaded(ListOfEditors[i]);
            }
        }
    };

    var allCSSLoaded = function(editor) {
        console.log("allcssloaded");
        var selector = "#" + editor.m_selectorid;
        editor.insertion($(selector)[0]);

        $(".rawbutton").click(function () {
            $(".rulebutton").css("visibility","hidden");
            editor.m_editor.doc.cantEdit = false;
            editor.m_editor.setOption("theme", "default");
            $(this).addClass("active");
            $(this).parent().children(".cornipicklebutton").removeClass("active");
        });

        $(".cornipicklebutton").click(function () {
            $(".rulebutton").css("visibility","visible");
            editor.m_editor.doc.cantEdit = true;
            editor.m_editor.setOption("theme", "rubyblue default");
            $(this).addClass("active");
            $(this).parent().children(".rawbutton").removeClass("active");
        });
    };

    var insertStylesheets = function() {
        var link1 = document.createElement('link');
        link1.setAttribute("rel", "stylesheet");
        link1.setAttribute("type", "text/css");
        link1.onload = function(){ codeMirrorBaseCSSLoaded(); }
        link1.setAttribute("href", "{% static "bower_components/codemirror/lib/codemirror.css" %}");
        document.getElementsByTagName("head")[0].appendChild(link1);

        var link2 = document.createElement('link');
        link2.setAttribute("rel", "stylesheet");
        link2.setAttribute("type", "text/css");
        link2.onload = function(){ fiddleCSSLoaded(); }
        link2.setAttribute("href", "{% static "css/fiddle/fiddle.css" %}");
        document.getElementsByTagName("head")[0].appendChild(link2);

        var link3 = document.createElement('link');
        link3.setAttribute("rel", "stylesheet");
        link3.setAttribute("type", "text/css");
        link3.onload = function(){ themeCSSLoaded(); }
        link3.setAttribute("href", "{% static "bower_components/codemirror/theme/rubyblue.css" %}");
        document.getElementsByTagName("head")[0].appendChild(link3);

        var link4 = document.createElement('link');
        link4.setAttribute("rel", "stylesheet");
        link4.setAttribute("type", "text/css");
        link4.onload = function(){ corniColorsCSSLoaded(); }
        link4.setAttribute("href", "{% static "modules/codemirror/lib/codemirror.css" %}");
        document.getElementsByTagName("head")[0].appendChild(link4);
    };

    var checkStylesheetsLoaded = function(newEditor) {
        console.log("check");
        if(Stylesheets["codeMirrorBase"] && Stylesheets["theme"] && Stylesheets["corniColors"] && Stylesheets["fiddle"]) {
            allCSSLoaded(newEditor);
        }
        else{
            setTimeout(checkStylesheetsLoaded(newEditor),1000);
        }
    };

    window.onload = function () {
        $(".fiddleEditor").each(function () {
            var count = 0;
            var t = $(this)[0];
            var text = t.firstElementChild.value;
            var id = t.firstElementChild.id;
            var name = t.firstElementChild.getAttribute("name");

            $.ajax({
                url: "{% url 'fiddle_editor' %}",
                type: "POST",
                data: {"text": text, "id": id, "name": name},
                success: function (html) {
                    insertStylesheets();
                    var h = document.createElement("div");
                    h.id = "codeMirrorInstance" + count; // Je donne ici un Id a un nouvelle élément
                    h.innerHTML = html;
                    $(t).children().first().replaceWith($(h));
                    var newEditor = new CodeMirrorEditor(count,id);
                    ListOfEditors[count] = newEditor;
                    count++;
                }
            });
        });

        $.ajax({
            url: "{% url 'get_grammar' %}",
            type: "POST",
            data: {"action": "getgrammar"},
            success: function (response) {
                Grammar = response;
            }
        });
    };
});

