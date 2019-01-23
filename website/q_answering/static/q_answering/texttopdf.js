/* Functionality for the editor and converting its contents to pdf*/

// Initialize editor
var editor = new Quill('#editor', {
    theme: 'snow'
});

var iframe = document.getElementById("examplePDFiframe");
var answerupdatevalue = document.getElementById("newanswer");

// Display the question answer upon opening the workspace.
updateeditorcontent();

// If text changes, update the pdf and create new preview
editor.on('text-change', function(){
    updateeditorcontent();
});

function printPDF() {
    iframe.contentWindow.print();
}

/* The inner HTML content is passed through and is checked for the
 * mark up language used to quote subquestions.
 */
function include_subquestions(answer_content)
{
    // Right now, subquestions are referenced by using [-subquestionnr-]
    while (answer_content.search(/\[\-\d+\-\]/i) != -1)
    {
        var markup = answer_content.match(/\[\-\d+\-\]/i);
        var markupstring = markup.toString();
        var markupdigit = markupstring.match(/\d+/i);
        var subquestionnr = parseInt(markupdigit) - 1;
        answer_content = answer_content.replace(/\[\-\d+\-\]/i,
                           subquestionlist[subquestionnr]);
    }
    return answer_content;
}

/* update editor content in the display Iframe, as well as in the form
 * field to save it to the database upon returning to overview.
 */
function updateeditorcontent()
{
    var contents = editor.root.innerHTML;
    answerupdatevalue.value = contents;
    iframe.contentDocument.write(); // Force firefox to load inner html
    iframe.contentDocument.close(); // after about:blank page.
    contents = include_subquestions(contents);
    var contenthtml = "<head></head> <body>".concat(contents, "</body>");
    iframe.contentDocument.documentElement.innerHTML = contenthtml;
}
