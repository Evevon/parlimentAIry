function panelToggleON()
{
    var panel, button;
    panel = document.getElementById("sidepanel");
    button = document.getElementById("sidepanelbtn");
    panel.style.display = "block";
    button.setAttribute('onclick', 'panelToggleOFF()');
    button.className = 'closeactivitybtn';
    button.innerHTML = '<i class="fas fa-times"></i>';
}

function panelToggleOFF()
{
    var panel, button;
    panel = document.getElementById("sidepanel");
    button = document.getElementById("sidepanelbtn");
    panel.style.display = "none";
    button.setAttribute('onclick', 'panelToggleON()');
    button.className = 'activitybtn';
    button.innerHTML = '<i class="fas fa-bars"></i>';
}
