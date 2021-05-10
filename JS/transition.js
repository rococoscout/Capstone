

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

  if(y <= (height*2.2) && y >= (height*1.5)){
    var opac = ((height*2.2)-y)/(height*2.2-height*1.5)
    // document.getElementById('chadtxt').innerHTML = "outside Bot: " + opac;

    $("#cloud_top").css("opacity",opac);
    $("#cloud_back").css("opacity",opac);
    $("#moon").css("opacity",opac);
    var margin = 1000 * (1-opac);
    var strmar = margin + "px";
    // $("#cloud_top").css('margin-right', strmar);
    // $("#cloud_back").css('margin-left', strmar);
    $("#moon").css('margin-top', strmar);
  }
  else if( y <= (height*1) && y >= (height*.2)){
    var opac = (y-(height*.2))/(height*1-height*.2)
    // document.getElementById('chadtxt').innerHTML = "outside top: " + opac;

    $("#cloud_top").css("opacity",opac);
    $("#cloud_back").css("opacity",opac);
    $("#moon").css("opacity",opac);
    var margin = -1000 * (1-opac);
    var strmar = margin + "px";
    // $("#cloud_top").css('margin-right', strmar);
    // $("#cloud_back").css('margin-left', strmar);
    $("#moon").css('margin-top', strmar);
  }
  else if((y <= (height*1.5)) && (y >= (height*1))){
    // document.getElementById('chadtxt').innerHTML = "in";
    $("#cloud_top").css("opacity",1);
    // $("#cloud_top").css('margin-right', "0%");
    $("#cloud_back").css("opacity",1);
    // $("#cloud_back").css('margin-left', "0%");
    $("#moon").css("opacity",1);
    $("#moon").css('margin-top', "0%");
  }
  else{
    // document.getElementById('chadtxt').innerHTML = "out";
    $("#cloud_top").css("opacity",0);
    // $("#cloud_top").css('margin-right',"-1000px");
    $("#cloud_back").css("opacity",0);
    // $("#cloud_back").css('margin-left',"-1000px");
    $("#moon").css("opacity",0);
    $("#moon").css('margin-top',"-1000px");
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
