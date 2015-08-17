$(document).ready(function() { 

    $(".animate_me")
    .mouseover(function() {
        $(this).stop().animate({width:600}, 500);
        $(this).children('.bold_me').css("font-weight", "bold");
    })
    .mouseout(function() {
        $(this).stop().animate({width:400}, 500);
        $(this).children('.bold_me').css("font-weight", "normal");
        
    });

});

