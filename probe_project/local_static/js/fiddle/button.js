var Button = function (elementNaming) {

    this.button = document.createElement("input");

    this.naming =  "";

    this.textArea = "";


    /*

    State : 1
        Un Editeur de texte qui n'est pas Codemirror

    State : 2
        Un Editeur de texte qui est Codemirror
     */
    this.state = 1;
    
    /*
    Regarde si l'element est une Class ou un ID
     */

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

    /*
    Ajoute le button à la page HTML
     */

    this.addButton = function() {
        this.button.type = "button";
        this.naming.appendChild(this.button);
    };

    /*
        Sauvegarde le text de l'ancien Editor a mettre dans l'instance de mirror
     */
    this.saveText = function(element){

        var textAreaInstance = document.getElementsByTagName("textarea");

        if (textAreaInstance.length === 1)
            this.textArea = document.getElementsByTagName("textarea")[0];
        else
            this.textArea = document.getElementById(element);

        // Ici l'editeur de text Change pour un CodeMirror
    };

    /*
    Return le statut de l'object Buttons
     */
    this.getStatue = function() {
        return this.state
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

    this.addFunctionOnClick = function(statut) {
        this.button.onclick = function (statut) {

            console.log("Patate");
            console.log("Patate");

            if (statut === 1 ){
                /*
                Ici l'interpreteur n'est pas encore  modifier (CodeMirror)
                 */
                var editor = CodeMirror.fromTextArea(document.getElementById("id_code"), {
                lineNumbers: true,
                mode: "xml",
                lineWrapping: true,
                theme: "hopscotch"
                // Nous devons Creer le highlight de Cornipickle et le mettre ici
                // Nous devons télécharger notre propre codemirroir
            }).setValue(this.naming);

                this.state = 2;
            }

            else if (this.state === 2){
                console.log("do Nothing !")

            }

        };
    };

    this.detectNaming(elementNaming);

};
