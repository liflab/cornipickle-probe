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
        var text = $(this)[0].firstElementChild.value;
        var id = $(this)[0].firstElementChild.id;
        var name = $(this)[0].firstElementChild.getAttribute("name");
        $(".fiddleEditor").load("http://localhost:8000/fiddle/fiddleeditor",{"text":text, "id":id, "name":name});

        var button = Button.Button("editorContainer");
    });


    
};

