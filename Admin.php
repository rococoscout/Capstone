<!--
********************************************************************************
Title: Admin Page for Chadbot
Author: Jess Lonetti
Purpose: To allow interface and management tools for the admins Chadbot.
Contact Information: rococoscout@gmail.com
Cited Sources:
  - Bootstrap 4.0.0 https://getbootstrap.com/

********************************************************************************
-->

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="description" content="Personal Portfolio">
    <meta name="keywords" content="Personal">
    <meta name="author" content="Jess Lonetti">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Website</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="./CSS/admin.css"
    <link rel="apple-touch-icon" sizes="180x180" href="favicon_package_v0.16/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="favicon_package_v0.16/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="favicon_package_v0.16/favicon-16x16.png">
    <link rel="manifest" href="favicon_package_v0.16/site.webmanifest">
    <link rel="icon" href="favicon_package_v0.16/safari-pinned-tab.svg" color="#5bbad5">
    <meta name="msapplication-TileColor" content="#00a300">
    <meta name="theme-color" content="#ffffff">
    <?php include 'PHP/Auth.php';?>
  </head>

<body>
  <!-- Button trigger modal -->
  <!-- Credit from: Bootstrap 4.0.0 website -->
  <div class="row">
    <div class="col">
      <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#addRule">
        Add Rule
      </button>
    </div>
    <div class="col">
    </div>
    <div class="col"></div>
  </div>

  <div class="row">
    <div class="col">
    </div>
    <div class="col">
      <input id="search" class="form-control" type="text" placeholder="Search...">
      <br>
      <br>
      <div id = "demo"></div>
    </div>
    <div class="col">
    </div>
  </div>



  <!-- Modal -->
  <div class="modal fade" id="addRule" tabindex="-1" role="dialog" aria-labelledby="addRuleTitle" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLongTitle">Add Rule Form</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <form>
            <div class="form-group">
              <label for="title_add">Title of Rule</label>
              <input class="form-control" id="title_add" placeholder="Proffessor Room Number">
            </div>
            <div class="form-group">
              <label for="rule_add">Regular Expression</label>
              <input  class="form-control" id="regex_add" placeholder="[wW]here.*[pP]rofessor.*room">
            </div>
            <div class="form-group">
              <label for="question_add">Example Questions</label>
              <textarea class="form-control" id="questions_add" rows="3" placeholder='Use "?" as a delimiter; example: Where is Proffessor Taylors room? Where is the location of Professor Taylors room?'></textarea>
            </div>
            <div class="form-group">
              <label for="rule">Answer</label>
              <input  class="form-control" id="answers_add" placeholder="Proffessor Taylor does not teach here anymore.">
            </div>
            <div class="form-group">
              <label for="description">Description</label>
              <textarea class="form-control" id="description_add" rows="3" placeholder="A rule that tells the user where a proffessor room is located"></textarea>
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>
          <button type="button" class="btn btn-primary" onclick="addrule()"  >Add Rule</button>
        </div>
      </div>
    </div>
  </div>

  <div class="modal fade" id="dltRule" tabindex="-1" role="dialog" aria-labelledby="dltRuleTitle" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLongTitle">Delete Rule</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div id="confirm">are you sure?</div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>
          <button type="button" class="btn btn-primary" onclick="deleterule()" >Delete Rule</button>
        </div>
      </div>
    </div>
  </div>

  <div class="modal fade" id="editRule" tabindex="-1" role="dialog" aria-labelledby="editRuleTitle" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLongTitle">Edit Rule Form</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
            <form>
              <div class="form-group">
                <label for="title_edit">Title of Rule</label>
                <input class="form-control" id="title_edit" placeholder="Proffessor Room Number">
              </div>
              <div class="form-group">
                <label for="regex_edit">Regular Expression</label>
                <input  class="form-control" id="regex_edit" placeholder="[wW]here.*[pP]rofessor.*room">
              </div>
              <div class="form-group">
                <label for="question_edit">Example Questions</label>
                <textarea class="form-control" id="questions_edit" rows="3" placeholder='Use "?" as a delimiter; example: Where is Proffessor Taylors room? Where is the location of Professor Taylors room?'></textarea>
              </div>
              <div class="form-group">
                <label for="answers_edit">Answer</label>
                <input  class="form-control" id="answers_edit" placeholder="Proffessor Taylor does not teach here anymore.">
              </div>
              <div class="form-group">
                <label for="description_edit">Description</label>
                <textarea class="form-control" id="description_edit" rows="3" placeholder="A rule that tells the user where a proffessor room is located"></textarea>
              </div>
            </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>
          <button type="button" class="btn btn-primary" onclick="editrule()">Edit Rule</button>
        </div>
      </div>
    </div>
  </div>

  <script src="JS/addbutton.js"></script>
</html>
