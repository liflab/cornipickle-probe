var open = false;

var ListOfEditors = [];

var CodeMirrorEditor = function() {
    this.m_editor = null;

    this.insertion = function(element) {
        this.m_editor = CodeMirror.fromTextArea(element,{
            lineNumbers:true,
            mode: "cornipickle",
            lineWrapping:true,
            theme: "rubyblue"
            // Nous devons Creer le highlight de Cornipickle et le mettre ici
            // Nous devons télécharger notre propre codemirroir
        });

        this.m_editor.on("change", this.onChange);
    };

    this.onChange = function(codemirror, obj) {
        console.log("EVENT");
    };

    this.restore = function() {
        var restore = this.m_editor.getTextArea();
        this.insertion(restore);
    }
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
                var newEditor = new CodeMirrorEditor();
                newEditor.insertion($(selector)[0]);

                $(".rawbutton").click(function () {
                    newEditor.m_editor.setOption("theme","hopscotch");
                    $(this).prop('disabled',true);
                    $(".cornipickleButton").prop('disabled',false)
                });

                $(".cornipickleButton").click(function () {
                    newEditor.m_editor.setOption("theme","rubyblue");
                    $(".rawbutton").prop('disabled',false);
                    $(this).prop('disabled',true);

                });
                ListOfEditors.push(newEditor);
            }
        });
        count++;
    });
};

