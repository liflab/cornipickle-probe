(function(){  
  var selector = "body p"; //change selector dynamically

  var elems = document.querySelectorAll(selector);

  for(var i = 0; i < elems.length; ++i){
    elems[i].addEventListener("click", function(e){
        var date = new Date();
        var trace = 
            {
              "event": {
                "date": date.toUTCString(),
                "click": {
                  "selector": selector
                }
              }
            };
        console.log(JSON.stringify(trace));
        send(JSON.stringify(trace)); //send to Probe site for processing
    }, false);
  }
})();