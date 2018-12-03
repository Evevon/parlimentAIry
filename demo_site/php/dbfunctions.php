<?php
include_once 'dbconnect.php';

/* getDBTable(str, connection) converts SQL table with name $tableName to php array.
 * Returns php 2 dimensional array.
 */
function getDBTable($tableName, $dbConn)
{
    $sql= "SELECT * FROM ".$tableName.";";
    $tableData = mysqli_query($dbConn, $sql);
    $dataArray = array();
    if (mysqli_num_rows($tableData) > 0)
    {
        while ($tableRow = mysqli_fetch_assoc($tableData))
        {
            $dataArray[] = $tableRow;
        }
    }
    return $dataArray;
}

/* convertTableRow(sql array row) takes a row from an sql array as input,
 * and converts this to a php array. Returns 2 dimensional php array.
 */
function convertTableRow($sqlRow)
{
    $dataArray = array();
    if (mysqli_num_rows($sqlRow) > 0)
    {
        while ($tableRow = mysqli_fetch_assoc($sqlRow)) {
            $dataArray[] = $tableRow;
        }
    }
    return $dataArray;
}

/* getCurrentQuestion(str, connection) gets the question with corresponding
 * id from the questions table. Returns 2 dimensional php array.
 */
function getCurrentQuestion($questionID, $dbConn)
{
    $sql = "SELECT * FROM questions WHERE id='".$questionID."';";
    $question = mysqli_query($dbConn, $sql);
    $row = convertTableRow($question);
    return $row;
}

/* updateCurrentQuestion(str, str, str, str, connection) updates the
 * value to newValue for a given property for an entry in a given table.
 */
function updateCurrentQuestion($table, $ID, 
            $property, $newValue, $dbConn)
{
    $sql = "UPDATE ".$table." SET ".$property."='".$newValue.
           "' WHERE id='".$ID."';";
    mysqli_query($dbConn, $sql);
}