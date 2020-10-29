document.getElementById('input').addEventListener("keyup", function(event) {

  if (event.keyCode === 13) {
    console.log("why")
    var text = document.getElementById('input').value;
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
      console.log(last)
      message = '<div class="message last">';
      message += text;
      message += '</div>';
      current[0].innerHTML += message;

    }
    document.getElementById('input').value = "";
  }



});
