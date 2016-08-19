var Button = function (elementNaming) {

    this.button = document.createElement("input");

    this.naming =  "";

    this.detectNaming = function(name) {
        if(typeof document.getElementsByClassName(name)[0] !== "undefined" ){
            this.naming = document.getElementsByClassName(name)[0];
        }
        else if (document.getElementById(name) !== null) {
            this.naming = document.getElementById(name);
        }
        else {
            console.log("Veuiller regarder la syntaxe de l'element dans le premier Parametre");
        }
    };

    this.addButton = function() {
        this.button.type = "button";
        this.naming.appendChild(this.button);
    };

    /*
     Ajout un Id Au bouton

     name : Un nom en string qui va deteminer l'id du bouton
     */
    this.addId =function (name) {
        this.button.id = name;
    };
    this.getInfo = function() {
        console.log("Naming: "+this.naming +"\n button : "+ this.button + "\n");
    };

    this.addFunctionOnClick = function(func) {
        this.button.onclick = function () {
            console.log("Button is Working !");
            var editor = CodeMirror.fromTextArea(document.getElementById("id_code"), {
                lineNumbers: true,
                mode: "javascript",
                lineWrapping: true,
                theme: "hopscotch"
                // Nous devons Creer le highlight de Cornipickle et le mettre ici
                // Nous devons télécharger notre propre codemirroir
            });
        };
    }

    this.changeMode = function(){
        console.log("Button is Working !");
        var editor = CodeMirror.fromTextArea(document.getElementById("id_code"),{
            lineNumbers:true,
            mode: "javascript",
            lineWrapping:true,
            theme: "hopscotch"
            // Nous devons Creer le highlight de Cornipickle et le mettre ici
            // Nous devons télécharger notre propre codemirroir
        });
    };

    this.detectNaming(elementNaming);

};
