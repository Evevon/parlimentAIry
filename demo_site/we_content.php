
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<!-- change stylesheet link to css/stylesheet.css if on mac or linux-->
<link rel="StyleSheet" href="css\stylesheet.css"type="text/css" media="all">

<!-- The work environment content, containing both the text editor and info screen-->
</head>

<frameset cols = "25%, 25%">
    <!-- Pass value of question ID to the frames -->
    <frame src="text_editor.php?questionid=<?php echo $_GET["questionid"]?>"/>
    <frame src="info_screen.php?questionid=<?php echo $_GET["questionid"]?>"/>
</frameset>
</html>

