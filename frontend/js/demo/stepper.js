
let curOpen;

$(document).ready(function() {
  curOpen = $('.step')[0];
  
  $('.next-btn').on('click', function() {
    let cur = $(this).closest('.step');
    let next = $(cur).next();
    var curInputs = cur.find(":input").filter('[required]:visible');
    var isValid = true;
    $(".form-control").removeClass("is-invalid");
    for(var i=0; i<curInputs.length; i++){
        if (!curInputs[i].validity.valid){
    console.log(curInputs[i]);
            isValid = false;
            $(curInputs[i]).closest(".form-control").addClass("is-invalid");
        }
    }

    if(isValid){
      $(cur).addClass('minimized');
      setTimeout(function() {
        $(next).removeClass('minimized');
        curOpen = $(next);
      }, 400);
    }
  });
  
  $('.close-btn').on('click', function() {
    let cur = $(this).closest('.step');
    $(cur).addClass('minimized');
    curOpen = null;
  });
  
  $('.step .step-content').on('click' ,function(e) {
    e.stopPropagation();
  });
  
  $('.step').on('click', function() {
    if (!$(this).hasClass("minimized")) {
      curOpen = null;
      $(this).addClass('minimized');
    }
    else {
      let next = $(this);
      if (curOpen === null) {
        curOpen = next;
        $(curOpen).removeClass('minimized');
      }
      else {
        $(curOpen).addClass('minimized');
        setTimeout(function() {
          $(next).removeClass('minimized');
          curOpen = $(next);
        }, 300);
      }
    }
  });
});