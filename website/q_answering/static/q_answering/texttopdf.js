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
    contents = include_subquestions(contents);
    var contenthtml = "<head></head> <body>".concat(contents, "</body>");
    iframe.contentDocument.documentElement.innerHTML = contenthtml;
});

function printPDF() {
    iframe.contentWindow.print();
}

/* The inner HTML content is passed through and is checked for the
 * mark up language used to quote subquestions.
*/
function include_subquestions(answer_content)
{
    //
    while (answer_content.search(/\[\-\d+\-\]/i) != -1)
    {
        var markup = answer_content.match(/\[\-\d+\-\]/i);
        var markupstring = markup.toString();
        var markupdigit = markupstring.match(/\d+/i);
        var subquestionnr = parseInt(markupdigit) - 1;
        answer_content = answer_content.replace(/\[\-\d+\-\]/i, subquestionlist[subquestionnr]);
    }
    return answer_content;
}
