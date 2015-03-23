$(document).ready(function() {

    updateCounter()

	setInterval(updateCounter(), 2500);
});

function updateCounter(){
    $.get('/update_count/', function(data) {
        $("#session_footer").html(data);
    })
}