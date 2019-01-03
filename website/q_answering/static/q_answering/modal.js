/* Functionality for the modal popups */


/* Change if more than one modal per page */
var modal = document.getElementById("modal");
var pagecontent =  document.getElementsByClassName("pagecontent")[0];


/* Have the modal pop up */
// At index page
function indexPopup(id, name, description)
{
    var nameSpot = document.getElementById('questionName');
    var descriptionSpot = document.getElementById('questionDescription');
    var answerButton = document.getElementById('questionAnswer');

    // Display corresponding question name and description in popup
    nameSpot.innerHTML = name;
    descriptionSpot.innerHTML = description;
    answerButton.value= id;

    modal.style.display = "block";
    pagecontent.className += " de-emphasized";
}

// At work environment page
function wePopup()
{
    modal.style.display = "block";
    pagecontent.className += " de-emphasized";
}


/* Have the modal close */
// By cancel button
function closePopup()
{
    modal.style.display = "none";
    pagecontent.className = pagecontent.className.replace(
                                " de-emphasized", "");
}

// By clicking outside of the modal popup
window.onclick = function(event)
{
    if (event.target == modal)
    {
        modal.style.display = "none";
        pagecontent.className = pagecontent.className.replace(
                                    " de-emphasized", "");
    }
}
