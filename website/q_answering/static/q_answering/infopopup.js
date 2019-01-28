function showpanel(title, content, popupID, nameSpotID, contentSpotID)
{
    var popup= document.getElementById(popupID);
    var nameSpot = document.getElementById(nameSpotID);
    var contentSpot = document.getElementById(contentSpotID);

    nameSpot.innerHTML = title;
    contentSpot.innerHTML = content;
    popup.style.display = "block";

}

function closepanel(panelname)
{
    var popup= document.getElementById(panelname);
    popup.style.display = "none";
}
