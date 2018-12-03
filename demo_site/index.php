<!-- Import php files: change to php/file.php when on mac/linux -->
<?php
    include_once "php\dynamichtml.php";
    include_once "php\dbconnect.php";
?>

<!DOCTYPE html>
<html>

<head>
<meta charset="UTF-8">
<!-- change stylesheet link to css/stylesheet.css if on mac or linux-->
<link rel="StyleSheet" href="css\stylesheet.css"type="text/css" media="all">
</head>

<body>
<div class="pagecontent">
        <!-- Banner at the top of the screen, containing logo and
            maybe user profile link -->
        <div class="banner">
            <!-- images/logo.png for mac/linux -->
            <img src="images\logo.png"></img>    
        </div>

        <!-- Workspace contains the four kanban zones that contain
             the questions -->
        <div class="workspace">

            <div class="kanbanzone" id="todo">
                <h3>te doen</h3>
                <div class="questionlist">
                    <ul>
                        <?php
                            echo generateQuestions($conn, 'todo');
                        ?>
                    </ul>
                </div>
            </div>

            <div class="kanbanzone" id="inprogress">
                <h3>in voortgang</h3>
                <div class="questionlist">
                    <ul>
                        <?php
                            echo generateQuestions($conn, 'inprogress');
                        ?>
                    </ul>
                </div>
            </div>

            <div class="kanbanzone" id="needverify">
                <h3>vereist verificatie</h3>
                <div class="questionlist">
                    <ul>
                        <?php
                            echo generateQuestions($conn, 'needverify');
                        ?>
                    </ul>
                </div>
            </div>

            <div class="kanbanzone" id="done">
                <h3>goedgekeurd</h3>
                <div class="questionlist">
                    <ul>
                        <?php
                            echo generateQuestions($conn, 'done');
                        ?>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <!-- Popup modal for clicking a question -->
    <div class="modal" id="modal">
        <div class="modal-content">
            
            <p>
                Weet u zeker dat u de vraag <span id="questionName"></span>
                wilt beantwoorden?
            </p>
            <br>
            <p id="questionDescription"></p>

            <div class="options">
                <!-- Redirect to work environment when getting confirmation -->
                <form action="workenvironment.php"
                      method="post">
                <button id="questionAnswer" name="id" type="submit" >
                    Beantwoord Vraag
                </button>
                </form>

                <!-- Cancel will close popup -->
                <button onclick="closePopup()">
                    Annuleer
                </button>
            </div>
        </div>
    </div>

<!-- Javascript file that regulates the modal functionality
     js/modal.js for mac/linux-->
<script src="js\modal.js"></script>


</body>
</html>