

var mainHeader = ["Title","Description","Priority","Options"];


function ltor(header,importlist){
  window.list  = JSON.parse(importlist);
  message = '<div class="row header-row">';
  size =  [2,6,2,2];
  for(a in header){
    message += '<div class="col-'+size[a]+'">'+ header[a] + '</div>';
  }
  message += '</div><hr>';
  console.log(list);
  for(i in list){
    flagger = false;
    message += '<div class="row" id="'+list[i]["idRules"]+'">';
    message += '<div class="col-2 table">';
    message += list[i]["title"];
    message+= '</div>';
    message += '<div class="col-6 table">';
    message += list[i]["description"];
    message+= '</div>';
    message += '<div class="col-2 table">';
    message += '<div class="dropdown"><button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">'+list[i]["priority"]+'</button><div class="dropdown-menu" aria-labelledby="Priority"><a class="dropdown-item" >1</a><a class="dropdown-item" >2</a><a class="dropdown-item" >3</a><a class="dropdown-item" >4</a><a class="dropdown-item" >5</a></div></div>';
    message+= '</div>';
    message+= '<div class="col-2 table">';
    message+= '<img src="./PIC/delete.png" class="delete" data-toggle="modal" data-target="#dltRule" onclick="storeid('+list[i]["idRules"]+')">';
    message+= '<img src="./PIC/edit.png" class="edit" data-toggle="modal" data-target="#editRule" onclick="storeid('+list[i]["idRules"]+','+i+')">';
    message+= '<img src="./PIC/graph.png" class="graph" onclick="graphrule('+list[i]["idRules"]+')">';
    for (ii in list[i]["answers"]){
      if(list[i]["answers"][ii]["flagCount"])
        flagger=true;
    }
    if(flagger){
      message+= '<img src="./PIC/flag.png">';
    }
    message+='</div>';

    message+= '</div>';
  }
  return message;
}
var initializevalues = {};
// Expects plain list no need to parse
function Btmkr(header,Entrylist){




  // console.log(header);

  message = '<div class="row header-row" >';
  for(aa in header){
      message += '<div class="col">'+header[aa]+'</div>';
  }

  message += '<div class="col">Options</div></div><hr>';
  message+='<div id='+header[1]+'>';
  for(i in Entrylist){

    message += '<div class="row" id="'+header[1]+"_"+Entrylist[i][header[0]]+'">';
    if(Entrylist[i][header[1]]==null){
      message+='</div>';
      initializevalues[Entrylist[i][header[0]]] = Entrylist[i][header[1]];
      continue;
    }
    // console.log(Entrylist[i]);

    message += '<div class="col-2">';
    message += Entrylist[i][header[0]];
    message+= '</div>';
    message += '<div class="col-6">';
    message += '<textarea  class="form-control editval" rows="2" id="'+Entrylist[i][header[0]]+'">'+Entrylist[i][header[1]]+'</textarea>';
    message+= '</div>';
    message+= '<div class="col-4">';
    message+= '<button type="button" class="btn btn-danger" onclick=\'deleteEntry('+Entrylist[i][header[0]]+',"'+header[1]+'")\'>Delete</button>'
    message+= '<button type="button" class="btn btn-secondary" onclick=\'editEntry('+Entrylist[i][header[0]]+',"'+header[1]+'")\'>Save</button>'

    if (header[1]=='answer')
      if(Entrylist[i]["flagCount"])
        message+= '<b style="color:red;">   '+Entrylist[i]["flagCount"]+'</b>';


    message+='</div>';
    message+= '</div>';

    initializevalues[Entrylist[i][header[0]]] = Entrylist[i][header[1]];
  }
  message+= '</div>';
  return message;

}

function ClearUnmatched(){
  var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
       document.getElementById('Unmatched').innerHTML = Umkr(JSON.parse(this.response));
      }
    };
    xhttp.open("POST", "http://10.1.83.57:5000/api/unmatched/clear", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send();
  displayunmatched();
}

function Umkr(body){
  message = '<div class="row header-row" >';
  message += '<div class="col">Unmatched Question</div>';
  message += '<div class="col">Count</div>';
  message += '</div>';

  for(i in body){
    message += '<div class="row" >';
    message += '<div class="col">'+body[i]["question"]+'</div>';
    message += '<div class="col">'+body[i]["count"]+'</div>';
    message += '</div>';
  }
  return message;
}

function Hmkr(body){
  message = "";

  for(i in body){
    message += '<b>'+body[i]["dateCreated"]+'</b>';
    message += '<div class="row" >';
    message += '<div class="col-xlg">User: '+body[i]["question"]+'</div>';
    message += '</div>';
    message += '<div class="row" >';
    message += '<div class="col-xlg">Chadbot: '+body[i]["answer"]+'</div>';
    message += '</div>';
  }
  return message;

}

displayrules();
displayunmatched();
displayhistory();

function displayunmatched(){
  button = '<button type="button" class="btn btn-light" onclick="ClearUnmatched()">Clear Unmatched Rules</button>';
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     document.getElementById('Unmatched').innerHTML = button+ Umkr(JSON.parse(this.response));
    }
  };
  xhttp.open("POST", "http://10.1.83.57:5000/api/unmatched/list", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send();
}

function displayhistory(){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      console.log(JSON.parse(this.response));
     document.getElementById('History').innerHTML = Hmkr(JSON.parse(this.response));
    }
  };
  xhttp.open("POST", "http://10.1.83.57:5000/api/rule/pairs", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send();
}

function displayrules(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
       document.getElementById("Rule").innerHTML = ltor(mainHeader,this.responseText);
       document.getElementById("Rule").style.color = "white";
       console.log("new");
       $(".dropdown-item").on("click",function(event){this.parentNode.parentNode.childNodes[0].innerHTML=this.innerHTML;editPriority(this.parentNode.parentNode.parentNode.parentNode.id,this.innerHTML);});

      }
    };
    xhttp.open("GET", "http://10.1.83.57:5000/api/entries/rules", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send();
  }

function editrule(id){
  // console.log(id);
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      displayrules();
    }
  };
  xhttp.open("POST", "http://10.1.83.57:5000/api/entries/rules/edit/rule", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("id="+id+"&title="+document.getElementById('title_edit').value+"&description="+document.getElementById('description_edit').value);

}

function addrule(){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    //  console.log(this.responseText);
    displayrules();
    }
  };
  var questions = document.getElementById('questions_add').value.trim();
  var answers  = document.getElementById('answers_add').value.trim();
  var regexes = document.getElementById('regex_add').value.trim();


  if (questions[questions.length-1] == "\n")
    questions = questions.substr(0,questions.length-1);

  if (regexes[regexes.length-1] == "\n")
    regexes = regexes.substr(0,regexes.length-1);

  if (answers[answers.length-1]=="\n")
    answers = answers.substr(0,answers.length-1);

  // console.log(answers)
  var listRegexes = JSON.stringify(regexes.split("\n"));
  var listQuestions = JSON.stringify(questions.split("\n"));
  var listAnswers = JSON.stringify(answers.split("\n"));
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
    console.log(newid);
    id = newid;
    // console.log(list);
    // console.log(newid);
    // console.log(loc);
   document.getElementById('title_edit').value= list[loc]["title"];
   document.getElementById('description_edit').value= list[loc]["description"];
   document.getElementById('regex_edit').innerHTML = Btmkr(['idRegexes','regex'],list[loc]['regexes']);
   document.getElementById('regex_edit').innerHTML +='<button type="button" class="btn btn-primary"  data-toggle="modal" data-target="#addmdl" id="Regexes" onclick=\'addEntry('+id+',"Regexes"'+')\' >Add Regex</button>' ;
   document.getElementById('answers_edit').innerHTML=Btmkr(['idAnswers','answer'],list[loc]['answers']);
   document.getElementById('answers_edit').innerHTML+= '<button type="button" class="btn btn-primary"  data-toggle="modal" data-target="#addmdl" id="Answers" onclick=\'addEntry('+id+',"Answers"'+')\'>Add Answer</button>';
   document.getElementById('questions_edit').innerHTML=Btmkr(['idQuestions','question'],list[loc]['questions']);
   document.getElementById('questions_edit').innerHTML+= '<button type="button" class="btn btn-primary"  data-toggle="modal" data-target="#addmdl" id="Questions" onclick=\'addEntry('+id+',"Questions"'+')\'>Add Question</button>';
   document.getElementById('questions_edit').innerHTML+= '<button type="button" class="btn btn-dark" onclick=\'showUQ("'+newid+'","'+loc+'")\'>View Unapproved Questions</button>';
   document.getElementById("edit_footer").innerHTML='<button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button><button type="button" class="btn btn-primary" data-dismiss="modal" onclick="editrule('+id+')">Done</button>';
   $(".editval").keyup(function(event){

     if(this.value != initializevalues[this.id]){
       this.style.border= "1px solid red";
     }
     else{
       this.style.border= "1px solid #ced4da";
     }
    });
  }



function deleterule(){
  // console.log(id);
  console.trace();
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    //  console.log(this.responseText);
    displayrules();
    }
  };


  xhttp.open("POST", "http://10.1.83.57:5000/api/entries/rules/delete", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("id="+id);

  $('#dltRule').modal('hide')
}

function editEntry(id,table){
  transfer = {"question":"Questions","answer":"Answers","regex":"Regexes"};
  tablename = transfer[table];
  // console.log(id+', '+tablename+', '+document.getElementById(id).value);
  var xhttp1 = new XMLHttpRequest();
   xhttp1.onreadystatechange = function() {
     if (this.readyState == 4 && this.status == 200) {
      // console.log("Working!!");
      initializevalues[id] = document.getElementById(id).value;
      document.getElementById(id).style.border="1px solid #ced4da";
     }
   };
   xhttp1.open("POST", "http://10.1.83.57:5000/api/entries/rules/edit/update", true);
   xhttp1.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
   xhttp1.send("id="+id+"&table="+tablename+"&update="+document.getElementById(id).value);

}

function deleteEntry(id,table){
  transfer = {"question":"Questions","answer":"Answers","regex":"Regexes"};
  tablename = transfer[table];
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      $("#"+table+"_"+id).remove();
    }
  };
  xhttp.open("POST", "http://10.1.83.57:5000/api/entries/rules/edit/delete", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("id="+id+"&table="+tablename);
}

function addEntry(newid,tablename){
  // console.log(tablename);
  // console.log(newid);

  document.getElementById('add-footer').innerHTML = '<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#editRule" data-dismiss="modal" onclick=\'addfinalize('+newid+',"'+tablename+'")\' >Add</button>';
  $('#editRule').modal('hide');
  }

function addfinalize(id,tablename){
  transferback = {"Questions":"question","Answers":"answer","Regexes":"regex"};
  eleid =transferback[tablename];
  // console.log(id);
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      $('#addmdl').modal('hide');
      dictid=JSON.parse(this.responseText);
      // console.log(dictid)
      addcol = "";

      for(i in dictid){
        console.log(dictid);
        console.log(dictid[i]);
        console.log(dictid[i]["Id"+tablename]);
        addcol = '<div class="row" id="'+eleid+"_"+dictid[i]["Id"+tablename]+'">';
        addcol += '<div class="col-2">';
        addcol += dictid[i]["Id"+tablename];
        addcol+= '</div>';
        addcol += '<div class="col-6">';
        addcol += '<textarea  class="form-control editval" rows="2" id="'+tablename+'">'+document.getElementById('addEntryText').value+'</textarea>';
        addcol+= '</div>';
        addcol+= '<div class="col-4">';
        addcol+= '<button type="button" class="btn btn-danger" onclick=\'deleteEntry("'+dictid[i]["Id"+tablename]+'","'+eleid+'\")\'>Delete</button>'
        addcol+= '<button type="button" class="btn btn-secondary" onclick=\'editEntry("'+dictid[i]["Id"+tablename]+'","'+eleid+'")\'>Save</button>'
        addcol+='</div>';
      }
      addcol+="</div>";
      document.getElementById(eleid).innerHTML+=addcol;
      document.getElementById('addEntryText').value = "";
    }
  };
  xhttp.open("POST", "http://10.1.83.57:5000/api/entries/rules/edit/add", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("id="+id+"&table="+tablename+"&newitem="+document.getElementById('addEntryText').value);
}


document.getElementById('search').addEventListener("keyup", function(event) {


    var text = document.getElementById('search').value;
    // console.log(text);
    if(text == ""){
      displayrules();
      exit();
    }
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        list = ltor(mainHeader,this.responseText);
        document.getElementById("Rule").innerHTML = ltor(mainHeader,this.responseText);
      }
    };
    xhttp.open("POST", "http://10.1.83.57:5000/api/rules/search", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("search="+text.toLowerCase());

});

function showUQ(id,loc){
  table = '<div class="row header-row" >';
  table += '<div class="col">Question</div><div class="col">Count</div>';
  table += '</div>';
  console.log(list[loc]);
  console.log(id);
  x_questions = list[loc]['x_questions'];
  for(i in x_questions){
    table += '<div class="row">';
    table += '<div class = "col">'+x_questions[i]['question']+'</div>';
    table += '<div class = "col">'+x_questions[i]['count']+'</div>';
    table += '</div>';
  }
  document.getElementById('tableofQuestions').innerHTML = table;
  $('#listQ').modal('show');
  $('#editRule').modal('hide');
}

function editPriority(id,priority){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {

    }
  };
  xhttp.open("POST", "http://10.1.83.57:5000/api/priority/update", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("id="+id+"&priority="+priority);
}
