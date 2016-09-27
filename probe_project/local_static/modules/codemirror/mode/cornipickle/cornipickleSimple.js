/*
 *   J'ai désidé de faire un module CornipickleSimple pour l'éditeur
 *
 *   Pourquoi je n'ai pas modifier le Bower_component ?
 *
 *       Les gens n'avait pas acces a mon bower_component local. J'aurais pu faire un fork du Projet codemirror et enregistrer
 *       un nouveau module bower. Il aurait fallu que quelqu'un gère le projet. Cette option serait p-t fiable plus tard
 * */


/**
 * Created by daehli on 24/08/16.
 */

require.config({
    packages: [{
        name: "codemirror",
        location: "/static/bower_components/codemirror",
        main: "lib/codemirror"
    }]
});

require(["codemirror",
    "codemirror/addon/mode/simple"],function (CodeMirror) {

    CodeMirror.defineSimpleMode("cornipickleSimple", {
        // The start state contains the rules that are initially used
        // The start state contains the rules that are initially used
        start: [
            // The regex matches the token, the token property contains the type
            // You can match multiple tokens at once. Note that the captured
            // groups must span the whole string in this case
            {
                regex: /(function)(\s+)([a-z$][\w$]*)/,
                token: ["keyword", null, "variable-2"]
            },
            // Rules are matched in the order in which they appear, so there is
            // no ambiguity between this one and the one above
            {
                regex: /0x[a-f\d]+|[-+]?(?:\.\d+|\d+\.?\d*)(?:e[-+]?\d+)?/i,
                token: "number"
            },
            {regex: /#.*/, token: "comment"},
            {regex: /^"[^"]+"/, token: "string"}, // trouver une meilleur methode pour détecter une string vide
            // A next property will cause the mode to move to a different state
            {regex: /"{3}/, token: "comment", next: "comment"},
            {regex: /(?:we say that|We say that)\b/, token: "keyword", next:"variable"},
            {regex: /(?:such that)\b/, token: "keyword"},
            {regex:/ in /,token:"keyword",next:"setname"},
            {regex: /(?:For each|for each|there exists|There exists|When|when|let|Let|The media query|applies|is now|be)\b/, token: "keyword"},
            {regex: /(?:And|If|Or|Then|Always|Not|Never|Next|Eventually|Eventually within|seconds|The next time|equals)\b/, token: "keyword"},
            {regex: /(?:is|greater than|less than|matches)\b/, token: "keyword-cornipickle"},
            {regex: /(\'s)\s(?:nodeValue|value|height|width|top|left|right|bottom|color|id|text|background|border|event|cornipickleid|display|size|accesskey|checked|disabled|min)\b/, token: "css-selector"},
            {regex:/^\$[\w\d]+/,token:"variable-cornipickle"}, // Notre variable
            {regex: /[-+\/*=<>!]+/, token: "operator"},
            // indent and dedent properties guide autoindentation
            {regex: /[\(]/, indent: true},
            {regex: /[\)]/, dedent: true},
            // You can embed other modes with the mode property. This rule
            // causes all code between << and >> to be highlighted with the XML
            // mode.
            {regex: /<</, token: "meta", mode: {spec: "xml", end: />>/}}
        ],
        // The multi-line comment state.
        comment: [
            {regex: /.*?"{3}/, token: "comment", next: "start"},
            {regex: /.*/, token: "comment"}
        ],
        // The meta property contains global information about the mode. It
        // can contain properties like lineComment, which are supported by
        // all modes, and also directives like dontIndentStates, which are
        // specific to simple modes.
        variable: [
            // Cette Regex est liée avec la Regex We say that
            {regex:/^\$[\w\d]+/,token:"variable-cornipickle"},
            {regex:/when/,token:"keyword",next:"start"}
        ],

        setname: [
            // <set_name> css Selector
            {regex:/\$\(([^\)]*)\)/,token:"jQuery",next:"start"},
            {regex:/^[\w\u0023\.\*\-]+/,token:"keyword",next:"start"}
        ],

        meta: {
            dontIndentStates: ["comment","variable"],
            lineComment: "//"
        }
    });
})

// https://regex101.com/r/mW1bF2/1 (comment)