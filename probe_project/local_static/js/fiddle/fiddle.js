var open = false;

/*

 */
var Button = function (elementNaming) {

    this.button = document.createElement("button");

    this.naming =  document.getElementsByClassName(elementNaming);

    this.style = []; // Style a ajouter

    this.color = ""; // Color

    this.statut = ""; // Open & Close

    this.type = "";



    var Button  = function(elementNaming){
        addButton();
    };

    var privateMethod = function () {
        // private
    };

    var applyStyle = function () {
        button.style = this.style
    };



    var addButton = function() {
        this.naming.appendChild(this.button);
    };

    var addStyle = function (stylebuttom) {
        // public
        style.push(stylebuttom)



    };

    var anotherMethod = function () {
        // public
    };

    return {
        Button:Button,
        anotherMethod: anotherMethod
    };


};

var editor;

var CMInsertion = function(element) {
    editor = CodeMirror.fromTextArea(element,{
        lineNumbers:true,
        mode: "javascript",
        lineWrapping:true,
        theme: "hopscotch"
        // Nous devons Creer le highlight de Cornipickle et le mettre ici
        // Nous devons télécharger notre propre codemirroir
    });
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
                CMInsertion($(selector)[0]);
            }
        });
        //var button = Button.Button("editorContainer");
    });
    
};

