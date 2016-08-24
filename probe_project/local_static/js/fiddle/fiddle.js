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

var CodeMirrorEditor = function(id) {
    this.m_editor = null;

    this.id = id;

    this.insertion = function(element) {
        this.m_editor = CodeMirror.fromTextArea(element,{
        lineNumbers:true,
        mode: "javascript",
        lineWrapping:true,
        theme: "hopscotch"
        // Nous devons Creer le highlight de Cornipickle et le mettre ici
        // Nous devons télécharger notre propre codemirroir
        });

        if(this.m_editor.getDoc().getValue() === "") {
            var scroller = this.m_editor.getScrollerElement();
            var elem = document.createElement("a");
            this.m_editor.getDoc().replaceRange("<S>\n.",{line:0,ch:0},{line:0,ch:0});
            var pos = this.m_editor.charCoords({line: 0, ch: 0}, "local");
            var endPos = this.m_editor.charCoords({line:0,ch:3},"local");
            elem.setAttribute("class", "startingrule rulebutton");
            elem.setAttribute("style", "top:" + pos.top + "px;left:" + pos.left + "px;width:" + (endPos.left-pos.left) +
                "px;height:20px;");
            elem.setAttribute("token","<S>");
            elem.setAttribute("editorid",this.id);
            $(scroller).find(".CodeMirror-sizer").append(elem);
        }
        this.m_editor.on("change", this.onChange);
    }

    this.onChange = function(codemirror, obj) {
        console.log("EVENT");
    };

    this.ruleClicked = function(button) {
        console.log("Rule " + button.attr("token") + " of editor " + button.attr("editorid") +  " was clicked!");
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

$("body").on("click", ".rulebutton", function() {
    var ed = ListOfEditors[$(this).attr("editorid")];
    ed.ruleClicked($(this));
});

window.onload = function() {
    var button = new Button("fiddleEditor");

    button.addId("changeMode");
    button.addFunctionOnClick();
    button.addButton();
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
                var newEditor = new CodeMirrorEditor(ListOfEditors.length);
                newEditor.insertion($(selector)[0]);
                ListOfEditors.push(newEditor);
            }
        });
        //var button = Button.Button("editorContainer");
    });
};

