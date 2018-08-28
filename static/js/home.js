
        
$(document).ready(function(){

function typeWriter(text, i) {
 if (i < (text.length)) {
    $('#message').html(text.substring(0, i+1));
    i++;
    setTimeout(function(){
        typeWriter(text, i);
    }, 200);
}
}

typeWriter("TRACK...ORGANISE...PLAN", 0);       
        
});