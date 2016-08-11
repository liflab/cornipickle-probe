var open = false;

window.onload = function() {
    $(".fiddleEditor").each( function () {
        var text = $(this)[0].firstElementChild.value;
        var id = $(this)[0].firstElementChild.id;
        var name = $(this)[0].firstElementChild.getAttribute("name");
        $(".fiddleEditor").load("http://localhost:8000/fiddle/fiddleeditor",{"text":text, "id":id, "name":name});

    })
};

$('body').on('click', ".editorYellowButton", function() {
    if(!open) {
        $(".glyphicon-chevron-down").removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up")
        $('.editorDropup').animate({
            top: '-=' + $('.editorPropertyMetadata').height() + 'px'
        }, 300, function() {
            open = true;
        });
    }
    else {
        $(".glyphicon-chevron-up").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down")
        $('.editorDropup').animate({
            top: '+=' + $('.editorPropertyMetadata').height() + 'px'
        }, 300, function() {
            open = false;
        });
    }
});

