var open = false;

window.onload = function() {
    $(".fiddleEditor").load("http://localhost:8000/fiddle/fiddleeditor");
};

$('body').on('click', ".editorYellowButton", function() {
    if(!open) {
        $('.editorDropup').animate({
            top: '-=' + $('.editorPropertyMetadata').height() + 'px'
        }, 300, function() {
            open = true;
        });
    }
    else {
        $('.editorDropup').animate({
            top: '+=' + $('.editorPropertyMetadata').height() + 'px'
        }, 300, function() {
            open = false;
        });
    }
});

