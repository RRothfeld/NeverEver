$(document).ready(function() {
	setInterval(function(){
		$.get('/update_count/', function(data) {
			$("#session_footer").html(data);
		})
	}, 2500);
});