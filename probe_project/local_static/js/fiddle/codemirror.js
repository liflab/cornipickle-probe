
window.onload = function() {

    var test = document.getElementById("id_code");
    var editor = CodeMirror.fromTextArea(document.getElementById("id_code"),{
        lineNumbers:true,
        mode: "javascript",
        lineWrapping:true,
        theme: "hopscotch"
        // Nous devons Creer le highlight de Cornipickle et le mettre ici
        // Nous devons télécharger notre propre codemirroir
    });
};
