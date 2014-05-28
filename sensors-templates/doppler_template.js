(function(){  
    var avant = window.performance.now();
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "empty.html", false);
    xmlhttp.send();
    var temps = window.performance.now() - avant;
    var date = new Date();
    var trace = 
      {
        "event":{
          "date": date.toUTCString(),
          "doppler":{
            "responseTime": temps
          }
        }
      };
    console.log(JSON.stringify(trace));
    send(JSON.stringify(trace)); 
})();
