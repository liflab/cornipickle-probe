(function(){  
  var selector = "body p"; //change selector dynamically
  var attribute = "name"; //change attribute dynamically

  var elems = document.querySelectorAll(selector);

  for(var i = 0; i < elems.length; ++i){
    var date = new Date();
    var trace = 
      {
        "event":{
          "date": date.toUTCString(),
          "harvester":{
            "selector": selector,
            "attribute":{
              "name": attribute,
              "value": elems[i].getAttribute(attribute)
            }
          }
        }
      }; 
    console.log(JSON.stringify(trace));
    send(JSON.stringify(trace)); //send to Probe site for processing
  }
})();
