function createCORSRequest(method, url) {
  var xhr = new XMLHttpRequest();
  if ("withCredentials" in xhr) {

    // Check if the XMLHttpRequest object has a "withCredentials" property.
    // "withCredentials" only exists on XMLHTTPRequest2 objects.
    xhr.open(method, url, true);

  } else if (typeof XDomainRequest != "undefined") {

    // Otherwise, check if XDomainRequest.
    // XDomainRequest only exists in IE, and is IE's way of making CORS requests.
    xhr = new XDomainRequest();
    xhr.open(method, url);

  } else {

    // Otherwise, CORS is not supported by the browser.
    xhr = null;

  }
  return xhr;
}

function send(str){
  var xhr = createCORSRequest('POST', "http://localhost/javascript-probe/test_xhr.php");
  if (!xhr) {
    throw new Error('CORS not supported');
  }
  xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
  xhr.send("data=" + str);
}

send("yeah!");
