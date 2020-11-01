
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
   document.getElementById("demo").innerHTML = this.responseText;
  }
};
xhttp.open("POST", "PHP/admin.php", true);
xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
xhttp.send();


function addrule(){
  console.log("hello");
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     document.getElementById("demo").innerHTML = this.responseText;
    }
  };
  xhttp.open("POST", "PHP/admin.php", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("rule="+document.getElementById('rule').value+"&title="+document.getElementById('title').value+"&description="+document.getElementById('description').value);
  $('#exampleModalCenter').modal('hide')
  document.getElementById('title').value = "";
  document.getElementById('description').value="";
  document.getElementById('rule').value ="";
  console.log("bye");
}
