$("div").hide();

$("html").mousemove(function( event ) {
    $("div").fadeIn();
    

    stop();
    myFunction();
});

function myFunction() {
    myVar = setTimeout(function(){
        $("div").fadeOut();
    }, 1000);
}
function stop() {
    if(typeof myVar != 'undefined'){
        clearTimeout(myVar);
    }
}