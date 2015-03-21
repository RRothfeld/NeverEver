
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

	$('#likes').click(function(){
	    var title;
	    title = $(this).attr("data-title");
	    $.get('/neverever/like_statement/', {title: title}, function(data){
	               $('#like_count').html(data);
	               $('#likes').hide();
	    });
	});


	$("body").on('keypress', '.editable_name', function(event) {
		if(event.keyCode == 13) {
			event.preventDefault();
			var playernum;
			playernum = $(this).attr("data-playernum");
			var thisname;
			thisname = $(this).html();
			$.get('/set_name/', {stamp: playernum, name: thisname}, function(data) {
				$('#answer_zone').html(data);
			});
		}
	});



});
