/* Functionality for tab bars */

/* Toggle a tab and its content given the tab name */
function tabToggle(event, tabName)
{
    var i, tabcontent, tablinks;

    // Hide all types of tab content
    tabcontent = document.getElementsByClassName("infocontent");
    for (i = 0; i < tabcontent.length; i++)
    {
        tabcontent[i].style.display = "none";
    }

    // Set all tab links on inactive
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++)
    {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Display only the element that is toggled on, and put
    // its corresponding button on active.
    document.getElementById(tabName).style.display = "block";
    event.currentTarget.className += " active";
}
