
$(document).ready(function() {
	$('#add_button').click(function(){
		//var sid;
		//sid = $(this).attr("data-sid");
		$.get('/add_player/', function(data) {
			$('#answer_zone').html(data);
		});
	});


	setInterval(function(){
		$.get('/update_count/', function(data) {
			$("#session_footer").html(data);
		})
	}, 3000);	

});



