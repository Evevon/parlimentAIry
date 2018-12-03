<?php

/* This file establishes database connection. These are the
 * default values when testing locally with most devservers.
 * Change if necessary.
 */
$dbServername = "localhost";
$dbUsername = "root";
$dbPassword = "";
$dbName = "parlimentairy";

$conn = mysqli_connect($dbServername, $dbUsername, $dbPassword, $dbName);
