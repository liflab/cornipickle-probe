var open = false;

var ListOfEditors = {};

var Grammar = {};

var CodeMirrorEditor = function(id) {
    this.m_editor = null;

    this.m_id = id;

    this.insertion = function(element) {
        this.m_editor = CodeMirror.fromTextArea(element,{
            lineNumbers:true,
            mode: "cornipickleSimple",
            lineWrapping:true
        });

        if(this.m_editor.getDoc().getValue() === "") {
            $("#codeMirrorInstance"+this.m_id).find(".cornipicklebutton").addClass("active");
            var scroller = this.m_editor.getScrollerElement();
            var elem = document.createElement("a");
            this.m_editor.getDoc().replaceRange("<S>\n.",{line:0,ch:0},{line:0,ch:0});
            var pos = this.m_editor.charCoords({line: 0, ch: 0}, "local");
            var endPos = this.m_editor.charCoords({line:0,ch:3},"local");
            elem.setAttribute("class", "startingrule rulebutton");
            elem.setAttribute("style", "top:" + pos.top + "px;left:" + pos.left + "px;width:" + (endPos.left-pos.left) +
                "px;height:20px;");
            elem.setAttribute("token","<S>");
            elem.setAttribute("editorid",this.m_id);
            $(scroller).find(".CodeMirror-sizer").append(elem);
        }
        else {
            this.m_editor.setOption("theme","hopscotch");
            $("#codeMirrorInstance"+this.m_id).find(".rawbutton").addClass("active");
        }
        this.m_editor.on("change", this.onChange);
    };

    this.displayRuleToolbar = function(button) {
        var editorelem = $("#codeMirrorInstance"+this.m_id).find(".ruletoolbar")[0];
        editorelem.style.display = "block";
    };

    this.onChange = function(codemirror, obj) {
        console.log("EVENT");
    };

    this.ruleClicked = function(button) {
        this.displayRuleToolbar(button);
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
    ed.ruleClicked($(this)[0]);
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
            }
        });
        count++;
    });

    $.ajax({
        url: "http://localhost:8000/fiddle/getgrammar",
        type: "GET",
        success: function(response) {
            Grammar = response;
        }
    });
};

