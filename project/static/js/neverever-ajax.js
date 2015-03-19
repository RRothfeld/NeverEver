
$('#add_button').click(function(){
	//var sid;
	//sid = $(this).attr("data-sid");
	$.get('/add_player/', function(data) {
		$('#answer_zone').html(data);
	});
});
