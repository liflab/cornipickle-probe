var Cqs = function() {
    this.m_stylesheets = [];

    this.getCqsSheets = function() {
        var scripts = document.querySelectorAll("script");
        for(i = 0; i < scripts.length; i++) {
            if(scripts[i].getAttribute("type") === "text/cqs") {
                if(styles[i].src){
                    // retrieve the file content with AJAX and process it
                    var cqsinstance = this;
                    (function(){
                        var xhr = new XMLHttpRequest;
                        xhr.open("GET", styles[i].src, true);
                        xhr.send(null);
                        xhr.onload = function(){
                            cqsinstance.parse(xhr.responseText);
                            cqsinstance.apply();
                        }
                    })();
                }
            }
        }
    };

    this.parse = function(code) {

    };

    this.apply = function() {

    };
};