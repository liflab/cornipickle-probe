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
/*
    $(".fiddleEditor").each( function () {
        var text = $(this)[0].firstElementChild.value;
        var id = $(this)[0].firstElementChild.id;
        var name = $(this)[0].firstElementChild.getAttribute("name");
        $(".fiddleEditor").load("http://localhost:8000/fiddle/fiddleeditor",{"text":text, "id":id, "name":name});


    });
*/

};
