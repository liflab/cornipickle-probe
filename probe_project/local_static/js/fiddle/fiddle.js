require.config({
    packages: [{
        name: "codemirror",
        location: "/static/bower_components/codemirror",
        main: "lib/codemirror"
    }]
});

var waitForCodeMirrorCss = function(){
    var cssCodeMirrorMap = {};
    cssCodeMirrorMap["codeMirrorBase"] = false;
    cssCodeMirrorMap["corniColors"] = false;
    cssCodeMirrorMap["fiddle"] = false;
    cssCodeMirrorMap["theme"] = false;

    var stylesheets = [];
    var begin = 0;
    var rules = [];
    var initialTime = new Date().getTime();
    do {
        stylesheets = document.styleSheets;
        for(var i = begin; i < stylesheets.length; i++) {
            if (stylesheets.cssRules) {                    // Browser uses cssRules?
                rules = stylesheets[i].cssRules;         // Yes --Mozilla Style
            } else {                                      // Browser usses rules?
                rules = stylesheets[i].rules;            // Yes IE style.
            }

            var found = "";

            for(var j = 0; j < rules.length; j++) {
                if(!cssCodeMirrorMap["codeMirrorBase"]) {
                    if(rules[j].selectorText && rules[j].selectorText === ".CodeMirror") {
                        found = "codeMirrorBase";
                        break;
                    }
                }
                if(!cssCodeMirrorMap["corniColors"]) {
                    if(rules[j].selectorText && rules[j].selectorText === ".cm-s-default .cm-braket-cornipickle") {
                        found = "corniColors";
                        break;
                    }
                }
                if(!cssCodeMirrorMap["fiddle"]) {
                    if(rules[j].selectorText && rules[j].selectorText === ".editorContent") {
                        found = "fiddle";
                        break;
                    }
                }
                if(!cssCodeMirrorMap["theme"]) {
                    if(rules[j].selectorText && rules[j].selectorText === ".cm-s-rubyblue.CodeMirror") {
                        found = "theme";
                        break;
                    }
                }
            }

            if(found !== "") {
                cssCodeMirrorMap[found] = true;
            }
            begin++;
        }
        //if(new Date().getTime() - initialTime > 5000) {
        //    console.log("Couldn't load every css files for codemirror");
        //    break;
        //}
    }while(!(cssCodeMirrorMap["codeMirrorBase"] && cssCodeMirrorMap["corniColors"] && cssCodeMirrorMap["fiddle"] && cssCodeMirrorMap["theme"]));
};

//Require JS
require(["codemirror"],function (CodeMirror) {
    var open = false;

    var ListOfEditors = {};

    var Grammar = {};


    var CodeMirrorEditor = function (id) {
        this.m_editor = null;

        this.m_id = id;

        this.m_ruletoolbar = null;

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
        var ed = ListOfEditors[$(this).attr("editorid")];
        ed.ruleClicked($(this));
    });

    $("body").on("click", ".submitterminalbutton", function () {
        var ed = ListOfEditors[$(this).closest(".ruletoolbar").attr("editorid")];
        ed.terminalButtonClicked($(this));
    });

    $("body").on("click", ".submitnonterminalbutton", function () {
        var ed = ListOfEditors[$(this).closest(".ruletoolbar").attr("editorid")];
        ed.nonTerminalButtonClicked($(this));
    });

    window.onload = function () {
        $(".fiddleEditor").each(function () {
            var count = 0;
            var t = $(this)[0];
            var text = t.firstElementChild.value;
            var id = t.firstElementChild.id;
            var name = t.firstElementChild.getAttribute("name");

            $.ajax({
                url: "http://localhost:8000/fiddle/fiddleeditor",
                type: "POST",
                data: {"text": text, "id": id, "name": name},
                success: function (html) {
                    var h = document.createElement("div");
                    h.id = "codeMirrorInstance" + count; // Je donne ici un Id a un nouvelle élément
                    h.innerHTML = html;
                    $(t).children().first().replaceWith($(h));
                    waitForCodeMirrorCss();
                    var selector = "#" + id;
                    var newEditor = new CodeMirrorEditor(count);
                    newEditor.insertion($(selector)[0]);

                    $(".rawbutton").click(function () {
                        $(".rulebutton").css("visibility","hidden");
                        newEditor.m_editor.doc.cantEdit = false;
                        newEditor.m_editor.setOption("theme", "default");
                        $(this).addClass("active");
                        $(this).parent().children(".cornipicklebutton").removeClass("active");
                    });

                    $(".cornipicklebutton").click(function () {
                        $(".rulebutton").css("visibility","visible");
                        newEditor.m_editor.doc.cantEdit = true;
                        newEditor.m_editor.setOption("theme", "rubyblue default");
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
            data: {"action": "getgrammar"},
            success: function (response) {
                Grammar = response;
            }
        });
    };
});

