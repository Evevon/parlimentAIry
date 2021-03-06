<!-- Import php files: change to php/file.php when on mac/linux -->
<?php
    require_once "php\dbconnect.php";
    include_once "php\dbfunctions.php";
?>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<!-- change stylesheet link to css/stylesheet.css if on mac or linux-->
<link rel="StyleSheet" href="css\stylesheet.css"type="text/css" media="all">
</head>

<body>
    <!-- Tabbar contains the tabs that can be toggled to get to
         the different info screens-->
    <div class="tabbar" >
        <button class="tablinks" 
                onclick="tabToggle(event, 'currentQuestion')"
                id="defaultOpen">
                huidige vraag
        </button>

        <button class="tablinks"
                onclick="tabToggle(event, 'articles')">
                artikelen
        </button>

        <button class="tablinks"
                onclick="tabToggle(event, 'oldQuestions')">
                oude vragen
        </button>
    </div>

    <!-- This infoscreen part will display the contents with information-->
    <div class="infoscreen">
        <div id="currentQuestion" class="tabcontent"> 
            <?php
                $questionData = getCurrentQuestion($_GET["questionid"] , $conn);
                echo $questionData[0]['description'];
            ?>
        </div>

        <div id="articles" class ="tabcontent">
                Artikel overzicht
        </div>

        <div id="oldQuestions" class="tabcontent">
                Oude vraag overzicht
        </div>
    </div>

    <!-- Functionality for the tabs, changes content when new tab is clicked
         js/tabbar.js for mac/linux-->
    <script src="js\tabbar.js"></script>
    <script>
        document.getElementById("defaultOpen").click();
    </script>
</body>
</html>

