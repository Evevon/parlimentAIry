/* Functionality for the editor and converting its contents to pdf*/

// Initialize editor
var editor = new Quill('#editor', {
    theme: 'snow'
});


// create a pdf preview
var iframe = document.getElementById("examplePDFiframe");


// If text changes, update the pdf and create new preview
editor.on('text-change', function(){
    var contents = editor.root.innerHTML;
    iframe.contentDocument.write();
    iframe.contentDocument.close();
    var contenthtml = "<head></head> <body>".concat(contents, "</body>")
    iframe.contentDocument.documentElement.innerHTML = contenthtml;
});

function printPDF() {
    iframe.contentWindow.print();
}
