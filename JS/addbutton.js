var list;

function ltor(list){
  list  = JSON.parse(list);
  message = '<div class="row header-row"><div class="col-sm">Title</div><div class="col-sm">Description</div><div class="col-sm">Edit</div></div></div><hr>';
  console.log(list);
  for(i in list){
    message += '<div class="row">';

    message += '<div class="col table">';
    message += list[i]["title"];
    message+= '</div>';
    message += '<div class="col table">';
    message += list[i]["description"];
    message+= '</div>';
    message+= '<div class="col table">'
    message+= '<img src="./PIC/delete.png" class="delete" data-toggle="modal" data-target="#dltRule" onclick="storeid('+list[i]["id"]+')">'
    message+= '<img src="./PIC/edit.png" class="edit" data-toggle="modal" data-target="#editRule" onclick="storeid('+list[i]["id"]+','+i+')">'
    message+='</div>';

    message+= '</div><hr>';
  }
  return message;
}

var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
   document.getElementById("demo").innerHTML = ltor(this.responseText);
  }
};
xhttp.open("GET", "http://10.1.83.57:5000/api/entries/rules", true);
xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
xhttp.send();


function addrule(){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     console.log(this.responseText);
     var xhttp1 = new XMLHttpRequest();
     xhttp1.onreadystatechange = function() {
       if (this.readyState == 4 && this.status == 200) {
        document.getElementById("demo").innerHTML = ltor(this.responseText);
       }
     };
     xhttp1.open("GET", "http://10.1.83.57:5000/api/entries/rules", true);
     xhttp1.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
     xhttp1.send();
    }
  };
  var questions = document.getElementById('questions_add').value.trim();
  var answers  = document.getElementById('answers_add').value.trim();

  var regexes = document.getElementById('regex_add').value.trim();


  if (questions[questions.length-1] == "?")
    questions = questions.substr(0,questions.length-1);

  if (regexes[regexes.length-1] == "|")
    regexes = regexes.substr(0,regexes.length-1);

  if (answers[answers.length-1]==".")
    answers = answers.substr(0,answers.length-1);

  console.log(answers)
  var listRegexes = JSON.stringify(regexes.split("|"));
  var listQuestions = JSON.stringify(questions.split("?"));
  var listAnswers = JSON.stringify(answers.split("."));
  var Sendrule = "regexes="+listRegexes;
  Sendrule +="&title="+document.getElementById('title_add').value+"&description="+document.getElementById('description_add').value;
  Sendrule += "&questions="+listQuestions+"&answers="+ listAnswers;

  xhttp.open("POST", "http://10.1.83.57:5000/api/entries/addRule", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send(Sendrule);
  $('#addRule').modal('hide')
  document.getElementById('title_add').value = "";
  document.getElementById('description_add').value="";
  document.getElementById('regex_add').value ="";
  document.getElementById('questions_add').value="";
  document.getElementById('answers_add').value="";
}

var id;
function storeid(newid, loc){
  id = newid;

     var xhttp1 = new XMLHttpRequest();
     xhttp1.onreadystatechange = function() {
       if (this.readyState == 4 && this.status == 200) {
         var list = JSON.parse(this.responseText);
         console.log(list);
         document.getElementById('title_edit').value= list[loc]["title"];
         document.getElementById('description_edit').value= list[loc]["description"];
         document.getElementById('regex_edit').value = list[loc]['regexes'].join("|");
         document.getElementById('answers_edit').value=list[loc]['answers'].join(".")+'.';
         document.getElementById('questions_edit').value=list[loc]['questions'].join('?')+'?';
       }
     };
     xhttp1.open("GET", "http://10.1.83.57:5000/api/entries/rules", true);
     xhttp1.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
     xhttp1.send();



}

function deleterule(){
  console.log(id);
  console.trace();
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     console.log(this.responseText);
     var xhttp1 = new XMLHttpRequest();
     xhttp1.onreadystatechange = function() {
       if (this.readyState == 4 && this.status == 200) {
        document.getElementById("demo").innerHTML = ltor(this.responseText);
       }
     };
     xhttp1.open("GET", "http://10.1.83.57:5000/api/entries/rules", true);
     xhttp1.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
     xhttp1.send();
    }
  };


  xhttp.open("POST", "http://10.1.83.57:5000/api/entries/rules/delete", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("id="+id);

  $('#dltRule').modal('hide')
}

function editrule(){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     console.log(this.responseText);
     var xhttp1 = new XMLHttpRequest();
     xhttp1.onreadystatechange = function() {
       if (this.readyState == 4 && this.status == 200) {
        document.getElementById("demo").innerHTML = ltor(this.responseText);
       }
     };
     xhttp1.open("GET", "http://10.1.83.57:5000/api/entries/rules", true);
     xhttp1.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
     xhttp1.send();
    }
  };
  var questions = document.getElementById('questions_edit').value.trim();
  var answers  = document.getElementById('answers_edit').value.trim();

  var regexes = document.getElementById('regex_edit').value.trim();


  if (questions[questions.length-1] == "?")
    questions = questions.substr(0,questions.length-1);

  if (regexes[regexes.length-1] == "|")
    regexes = regexes.substr(0,regexes.length-1);

  if (answers[answers.length-1]==".")
    answers = answers.substr(0,answers.length-1);

  console.log(answers)
  var listRegexes = JSON.stringify(regexes.split("|"));
  var listQuestions = JSON.stringify(questions.split("?"));
  var listAnswers = JSON.stringify(answers.split("."));
  var Sendrule = "regexes="+listRegexes;
  Sendrule +="&title="+document.getElementById('title_edit').value+"&description="+document.getElementById('description_edit').value;
  Sendrule += "&questions="+listQuestions+"&answers="+ listAnswers;
  Sendrule += "&id=" + id;

  xhttp.open("POST", "http://10.1.83.57:5000/api/entries/rules/update", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send(Sendrule);

  $('#editRule').modal('hide')

}

document.getElementById('search').addEventListener("keyup", function(event) {

  if (event.keyCode === 13) {
    var text = document.getElementById('search').value;
    console.log(text);
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("demo").innerHTML = ltor(this.responseText);
        document.getElementById('search').value="";
      }
    };
    xhttp.open("POST", "http://10.1.83.57:5000/api/rules/search", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("search="+text.toLowerCase());


  }

});
