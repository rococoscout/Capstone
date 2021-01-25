

function ltor(list){
  list  = JSON.parse(list);
  console.log(list);
  message = '<div class="row header-row"><div class="col-sm">description</div><div class="col-sm">rule</div><div class="col-sm">ruleID</div><div class="col-sm">title</div></div>';
  for(i in list){
    message += '<div class="row">';
    console.log(i);
    for(ii in list[i]){

      message += '<div class="col-sm">';
      message += list[i][ii];
      message+= '</div>';

    }

    message+= '</div>';
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
  console.log("hello");
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
  xhttp.open("POST", "http://10.1.83.57:5000/api/entries/addRule", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("rule="+document.getElementById('rule').value+"&title="+document.getElementById('title').value+"&description="+document.getElementById('description').value);
  $('#exampleModalCenter').modal('hide')
  document.getElementById('title').value = "";
  document.getElementById('description').value="";
  document.getElementById('rule').value ="";
}
