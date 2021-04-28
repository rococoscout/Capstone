const sidebar = document.getElementById("sidebar");


function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.body.style.marginLeft = "250px";
  document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}



function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.body.style.marginLeft= "0";
  document.body.style.backgroundColor = "white";
}

function changeColor(){
  console.log(sidebar.body.style.backgroundColor());

}
