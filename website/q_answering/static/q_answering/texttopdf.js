/* Functionality for the editor and converting its contents to pdf*/

// Initialize editor
var editor = new Quill('#editor', {
    theme: 'snow'
});

// Default pdf export is a4 paper, portrait, using milimeters for units
var pdf = new jsPDF();
// create a downloadable pdf preview
var iframe = document.getElementById("examplePDFiframe");
iframe.src = pdf.output("datauristring");

// If text changes, update the pdf and create new preview
editor.on('text-change', function(){
    var pdf = new jsPDF();

    // fromHTML is deprecated and buggy, try to switch to addHTML
    pdf.fromHTML(editor.root.innerHTML, 30, 30);
    //pdf.addHTML();
    iframe.src = pdf.output("datauristring");
});
