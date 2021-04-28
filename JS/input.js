function resolveAfter1Seconds(){
  return new Promise(resolve => {
    setTimeout(()=>{
      resolve('resolved');
    },1000);
  });
}

async function thinking(response,id){
  console.log('calling');
  document.getElementById('text').innerHTML +='<div class="yours messages thinking"><div class="message thinking"><div id = "child1"></div><div id = "child2"></div><div id = "child3"></div>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</div></div>'
  tobot();
  const result = await resolveAfter1Seconds();
  $('.thinking').remove();
  document.getElementById('text').innerHTML += '<div class="yours messages"><div class="message last" id="'+id+'"onclick="flag('+id+')" data-toggle="tooltip" rel="tooltip" data-placement="top" title="Click on the text to flag for the admin">'+ response+'</div></div>';
  console.log('result');
  $(function () {
    $("[rel='tooltip']").tooltip();
  });
  tobot();
}

function flag(id){
  var link;
  if(document.getElementById(id).style.color=="red"){
    document.getElementById(id).style.color ="white";
    link = "/api/removeFlag";
  }
  else{
    document.getElementById(id).style.color ="red";
    console.log(document.getElementById(id));
    link = "/api/flag";
  }


  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {

    }
  };
  xhttp.open("POST", "http://10.1.83.57:5000"+link, true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("id="+id);
}

document.getElementById('input').addEventListener("keyup", function(event) {

  if (event.keyCode === 13) {
    var text = document.getElementById('input').value;
    if (text == "" || /^\s*$/.test(text))
      return;
    var message = "";
    var current = document.getElementsByClassName('current');
    console.log(current.length)
      if(current.length!=1){
      message = '<div class="mine messages current">';
      message += '<div class="message last">';
      message += text;
      message += '</div></div>';
      document.getElementById('text').innerHTML += message;
      }
      else{
        var last = current[0].getElementsByClassName('last')[0]
        last.classList.remove("last");
        message = '<div class="message last">';
        message += text;
        message += '</div>';
        current[0].innerHTML += message;

      }
    document.getElementById('input').value = "";
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
       details=JSON.parse(this.response);
       console.log(details);
       console.log(details[0]['idAnswers']);

       thinking(details[0]['answer'],details[0]['idAnswers']);

       current[0].classList.remove("current");

      }
    };
    xhttp.open("POST", "http://10.1.83.57:5000/api/input", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("input="+text.toLowerCase());

  }
  tobot();
  });


  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function (event) {
          event.preventDefault();

          document.querySelector(this.getAttribute('href')).scrollIntoView({
              behavior: 'smooth'
          });
      });
  });


function tobot(){

  document.getElementById('text').scrollTo(0,document.getElementById('text').scrollHeight);
}
