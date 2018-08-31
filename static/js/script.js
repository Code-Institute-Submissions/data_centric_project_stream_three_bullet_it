
        
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

 $(document).ready(function() {
            $('.collapsible').collapsible();
            $('select').material_select();
            $(".button-collapse").sideNav();
        });
        $('.datepicker').pickadate({
            format: 'dd-mm-yy',
            selectMonths: true, 
            selectYears: 15, 
            today: 'Today',
            clear: 'Clear',
            close: 'Ok',
            closeOnSelect: false 
        });
        
        
        
function forceLower(strInput) 
{
    strInput.value=strInput.value.toLowerCase();
}