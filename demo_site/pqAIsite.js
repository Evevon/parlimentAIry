
var modal = document.getElementById("test");

console.log(modal);

function popup() {
    modal.style.display = "block";
}

function closePopup() {
    modal.style.display = "none";
}

function redirectWorkEnvironment() {
    window.location.href = "workenvironment.html";
}

function redirectHome() {
    window.location.href = "index.html"
}

window.onclick = function(event) {
    if (event.target == modal)
    {
        modal.style.display = "none";
    }
}
