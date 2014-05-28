(function(){  
  var timeout = 1000; //Modifier dynamiquement
  var x = 0;
  var y = 0;
  document.addEventListener("mousemove", function(e){
    x = e.clientX;
    y = e.clientY;
  }, false);
  function sendMousePosition(){
    var date = new Date();
    var trace = 
      {
        "event":{
          "date": date.toUTCString(),
          "mousePosition":{
            "x": x,
            "y": y
          }
        }
      };
    console.log(JSON.stringify(trace));
    send(JSON.stringify(trace)); 
    setTimeout(sendMousePosition, timeout); 
  }
  setTimeout(sendMousePosition, timeout); 
})();
