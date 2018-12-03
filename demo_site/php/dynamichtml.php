<?php
include_once 'dbfunctions.php';

/* Generates the html for the questions in the questions table dynamically.
 * Returns generated html code.
 */
function generateQuestions($dbConn, $status)
{
    $html = '';
    $questionData = getDBTable("questions", $dbConn);
    foreach ($questionData as $question)
    {
        if ($question['status'] == $status)
        {
            $id = $question['id'];
            $name = $question['name'];
            $description = $question['description'];

            $html.= '<li class="question">'.
                        '<button onclick="indexPopup(&quot;'.$id.'&quot;,'.
                          '&quot;<i>'.$name.'</i>&quot;,'.
                          '&quot;<i>'.$description.'</i>&quot;)">'.
                            $name.
                        '</button>'.
                    '</li>';
        }
    }

    return $html;
}

