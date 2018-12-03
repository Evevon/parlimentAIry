<?php
include_once "dbfunctions.php";
include_once "dbconnect.php";

/* This code updates the question status after the user returns
 * to the home screen from the work environment.
 */
if(isset($_POST["btnInProgress"]))
{
   updateCurrentQuestion("questions",
                         $_POST["questionID"],
                         "status",
                         $_POST["btnInProgress"],
                         $conn);
}
else {
    updateCurrentQuestion("questions",
                           $_POST["questionID"],
                           "status",
                           $_POST["btnNeedVerify"],
                           $conn);
}

/* After database update, redirect to homepage.
 * change to "location: ../index.php if on linux/mac.
 */
header("location: ..\index.php ");
