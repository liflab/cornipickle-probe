function send(str){
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "test_xhr.php", true);
  xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
  xhr.send("data=" + str );
}

send("yeah!");
