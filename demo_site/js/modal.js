/* Functionality for the modal popups */


/* Change if more than one modal per page */
var modal = document.getElementById("modal");
var pagecontent =  document.getElementsByClassName("pagecontent")[0];


/* Have the modal pop up */
function popup() {
    modal.style.display = "block";
    pagecontent.className += " de-emphasized";
}


/* Have the modal close */
// By cancel button
function closePopup() {
    modal.style.display = "none";
    pagecontent.className = pagecontent.className.replace(" de-emphasized", "");
}

// By clicking outside of the modal popup
window.onclick = function(event) {
    if (event.target == modal)
    {
        modal.style.display = "none";
        pagecontent.className = pagecontent.className.replace(" de-emphasized", "");
    }
}


/* Functions of other modal buttons*/
// Link to work environment 
function redirectWorkEnvironment() {
    window.location.href = "workenvironment.html";
}

// Link to home page
function redirectHome() {
    window.location.href = "index.html"
}

