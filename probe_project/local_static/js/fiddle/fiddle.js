var open = false;

/*
 Class Button qui Creer un Element Button Dynamiquement

 elementNaming: Class sur lequel le button dois être ajouté. Faite bien attention de l'ajouter avec un Classe et non un ID

 */
/*

 var Button = function (elementNaming) {

 this.button = document.createElement("button");

 this.naming =  this.detectNaming(elementNaming) || "";

 this.detectNaming = function(name) {
 if(typeof document.getElementsByClassName(name)[0] !== "undefined" ){
 this.naming = document.getElementsByClassName(name)[0];
 }
 else if (typeof document.getElementById(name) !== "undefined") {
 this.naming = document.getElementById(name);
 }
 else {
 console.log("Veuiller regarder la sytaxe de l'element dans le premier Parametre");
 }
 };
 this.addButton = function() {
 this.button.innerHTML = "Click ME";
 this.naming.appendChild(this.button);
 };

 this.getInfo = function() {
 console.log("Naming: "+this.naming +"\n button : "+ this.button + "\n");
 };

 };
 */

var ListOfEditors = [];

var CodeMirrorEditor = function() {
    this.m_editor = null;

    this.insertion = function(element) {
        this.m_editor = CodeMirror.fromTextArea(element,{
        lineNumbers:true,
        mode: "javascript",
        lineWrapping:true,
        theme: "hopscotch"
        // Nous devons Creer le highlight de Cornipickle et le mettre ici
        // Nous devons télécharger notre propre codemirroir
        });

        this.m_editor.on("change", this.onChange);
    }

    this.onChange = function(codemirror, obj) {
        console.log("EVENT");
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




window.onload = function() {
    var button = new Button("fiddleEditor");

    button.addId("changeMode");
    button.addFunctionOnClick();
    button.addButton();
    button.getInfo();
    $(".fiddleEditor").each( function () {
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
                h.innerHTML = html;
                t.firstElementChild.parentNode.replaceChild(h,t.firstElementChild);
                var selector = "#" + id;
                var newEditor = new CodeMirrorEditor();
                newEditor.insertion($(selector)[0]);
                ListOfEditors.push(newEditor);
            }
        });
    });
};

