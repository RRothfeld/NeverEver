$(document).ready(function() {
	
	$('#add_button').click(function(){
		$.get('/add_player/', function(data) {
			$('#answer_zone').html(data["rendered"]);
            if (data["nPlayers"] >= 6){
                $('#add_button').hide();
            }
			//$.getScript("../../static/js/bootstrap-toggle.min.js");
		});
	});

	setInterval(function(){
		$.get('/update_count/', function(data) {
			$("#session_footer").html(data);
		})
	}, 2500);

	$('#likes').click(function(){
	    var title;
	    title = $(this).attr("data-title");
	    $.get('/like_statement/', {title: title}, function(data){
	               $('#like_count').html(data);
	               $('#likes').hide();
	    });
	});

	//initialise popover when page is loaded
	$(function() {
		$("[data-toggle='popover']").popover();
	});
	
	//reinitalise popover after ajax content is loaded
	$(document).ajaxComplete(function() {
		$(function() {
			$("[data-toggle='popover']").popover();
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
				//$.getScript("../../static/js/bootstrap-toggle.min.js");
			});
		}
	});

	$("body").on('click', '.editable_name', function(event) {
		$(this).html("");
		$(this).attr('contenteditable', true);
		$(this).focus();
	});

});