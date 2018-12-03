<?php
    include_once "php\dbfunctions.php";
    include_once "php\dbconnect.php";
?>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<!-- change stylesheet link to css/stylesheet.css if on mac or linux-->
<link rel="StyleSheet" href="css\stylesheet.css"type="text/css" media="all">
</head>

<body id="workenvironment">
    <div class="pagecontent">
        <!-- Banner at the top of the screen, containing logo and
            maybe user profile link -->
            <div class="banner">
                <!-- images/logo.png for mac/linux -->
                <img src="images\logo.png"></img>    
            </div>

        <!-- Work environment page content
             pass question ID value to the iframe -->
        <iframe src="we_content.php?questionid=
                <?php echo $_POST['id'] ?>"></iframe>

        <div class="options" id="we-options">
            <button onclick="wePopup()">
                klaar voor nu
            </button>
        </div>
    </div>

    <!-- Popup modal for exiting a question -->
    <div class="modal" id="modal">
        <div class="modal-content">
            <p>U keert nu terug naar het scherm, wat is de status van deze vraag?</p>

            <div class="options">
                <form action="php\updatequestion.php"
                      method="post">

                    <!-- Pass values for parameters necessary to
                         update question -->
                    <input type="hidden"
                           name="questionID"
                           value="<?php echo $_POST['id'] ?>"/>

                    <!-- Pass status value depending on what button
                         the user clicks -->
                    <button name="btnInProgress"
                            value="inprogress"
                            type="submit">
                        in voortgang
                    </button>

                    <button name="btnNeedVerify"
                            value="needverify"
                            type="submit">
                        vereist verificatie
                    </button>
                </form>

                <button onclick="closePopup()">
                    annuleer
                </button>
            </div>
        </div>
    </div>

    <!-- Javascript file that regulates the modal functionality
         js/modal.js for mac/linux-->
    <script src="js\modal.js"></script>
</body>
</html>