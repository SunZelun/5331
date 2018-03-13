<?php
define("HOST", "localhost");     // The host you want to connect to.
define("USER", "root");    // The database username.
define("PASSWORD", "");    // The database password.
define("DATABASE", "test");    // The database name.

$conn = new mysqli(HOST, USER, PASSWORD, DATABASE);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
