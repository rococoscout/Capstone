<?php
  // mysql.inc.php - This file will be used to establish the db connection
  class myConnectDB extends mysqli{
    public function __construct($hostname="midn.cs.usna.edu",
      $user="m215394",
      $password="greg1018",
      $dbname="m215394"){
      parent::__construct($hostname, $user, $password, $dbname);
    }
  }
?>
