

$(document.body).scroll(function(){
  var y = $(document.body).scrollTop();
  var height = window.innerHeight

  display = "y: " + y + "height: " + height;


  if(y<(height)){
    document.getElementById('chadtxt').innerHTML = "Hey my name is Chad!";
  }
  else if(y>=(height)&&y<(height*2)){
    document.getElementById('chadtxt').innerHTML = "That's me, pretty intresting right.";
  }
  else if(y>=(height*2)&&y<(height*3)){
    document.getElementById('chadtxt').innerHTML = "Wow look at those guys they really helped me get the hang of things around here.";
  }
  else{
    document.getElementById('chadtxt').innerHTML = "Let us know what we could do better on!";
  }


  if(y <= (height*3.3) && y >= (height*2.7)){
    var opac = ((height*3.3)-y)/(height*3.3-height*2.7)
    $("#about_us_body").css("opacity",opac);
    var top = height*.5 * (1-opac);
    var strtop = top + "px";
     $("#about_us_body").css('margin-top', strtop);
  }
  else if( y <= (height*2) && y >= (height*1.2)){
    var opac = (y-(height*1.2))/(height*2-height*1.2)
    $("#about_us_body").css("opacity",opac);
    var top = height*.5 * (opac-1);
    var strtop = top + "px";
     $("#about_us_body").css('margin-top', strtop);
  }
  else if((y <= (height*2.7)) && (y >= (height*2))){
    $("#about_us_body").css("opacity",1);
    $("#about_us_body").css('margin-top', "0px");
  }
  else{
    $("#about_us_body").css("opacity",0);
    var top = height*.5*(-1);
    var strtop = top +"px";
    $("#about_us_body").css('margin-top', strtop);
  }
});
