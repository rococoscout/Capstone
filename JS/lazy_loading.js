document.addEventListener("DOMContentLoaded", function(){
  var lazyimages = document.querySelectorAll("img.lazy");

  function lazyload(){
    lazyload = setTimeout(function(){
      lazyimages.forEach(function(img){
        var scrollTop = window.pageYOffset;
        if(img.offsetTop<(window.innerHeight + scrollTop)){
          img.src = img.dataset.src;
          img.classList.remove('lazy');
          }
      });
      if(lazyimages.length==0){
        document.removeEventListener("scroll",lazyload());
      }
    },500);
  }


  document.addEventListener("scroll",lazyload());
});



// Used CSS-Tricks.com for a template.
