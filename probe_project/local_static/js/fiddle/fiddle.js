var open = false;
$('#editorYellowButton').click(function() {
  $('#editorDropup').animate({
    top:'-100px'
  }, 500, function() {
    open = true;
  });
});