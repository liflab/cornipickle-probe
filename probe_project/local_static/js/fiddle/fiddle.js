var open = false;
$('#editorYellowButton').click(function() {
    $('#editorDropup').animate({
        top:'-100px'
    }, 500, function() {
        open = true;
    });
});

window.onload = function() {
    $(".fiddleEditor").load("http://localhost:8000/fiddle/fiddleeditor");
};