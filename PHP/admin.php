<?php
/* Author: MIDN 1/C Gregory Polmatier
 * Purpose: Handle the functions required by the Admin side of the
 * 	    Chadbot including adding to the database and querying.
 */ 

//MySQL Library
require_once('mysql.inc.php');

//connect to SQL Database
$db = new myConnectDB();

//if a rule is to be added
if (!empty($_POST["rule"])) {
   $rule = 		    $_POST["rule"];
   $title = 		    $_POST["title"];
   $description = 	    $_POST["description"];

   $sql = "INSERT INTO Rules (title, rule, description)
   	  	  VALUES (?, ?, ?)";

   $stmt = $db -> stmt_init();
   $stmt -> prepare($sql);
   $stmt -> bind_param('sss', $title, $rule, $description);

   $success = $stmt -> execute();

   if (!$success) {
      echo "<h5> ERROR: " . $db->error . " for *addRule*</h5>";
   }
}


 
/********display "Rule" db table*********/
$sql = "SELECT ruleID, title, rule, description
       	       FROM Rules";

$result = $db->query($sql);

//create an array and fill with table values 
$arr = array();
while( $row = $result->fetch_assoc($result) ) {
  $arr[] = $row;
}

//return json encoded array of the table
echo json_encode($arr);




