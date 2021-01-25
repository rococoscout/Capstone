function resolveAfter1Seconds(){
  return new Promise(resolve => {
    setTimeout(()=>{
      resolve('resolved');
    },1000);
  });
}

async function thinking(response){
  console.log('calling');
  document.getElementById('text').innerHTML +='<div class="yours messages thinking"><div class="message thinking"><div id = "child1"></div><div id = "child2"></div><div id = "child3"></div>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</div></div>'
  const result = await resolveAfter1Seconds();
  $('.thinking').remove();
  document.getElementById('text').innerHTML += '<div class="yours messages"><div class="message last">'+ response+'</div></div>';
  console.log('result');

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
       thinking(this.response);

       current[0].classList.remove("current");


      }
    };
    xhttp.open("POST", "http://10.1.83.57:5000/api/input", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("input="+text);
  }

  });
