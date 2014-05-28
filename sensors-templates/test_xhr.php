<?php
    header("Access-Control-Allow-Origin: http://localhost:8000");
        echo '$_POST='; 
        echo  var_dump($_POST);
        echo  ' $_GET=';
        echo var_dump($_GET);
    if($_POST["data"] === "yeah!"){
    }
?>
