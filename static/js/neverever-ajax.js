$(document).ready(function(data) {

    if ($('#No-statement').length){
        disableLike();
        disableAdd();
    }

    $.get('/get_game_data/', function(data) {
        checkNumPlayers(data);
    });

    //enable animated switches
    playSwitches();

	$('#add_button').click(function(){
		$.get('/add_player/', function(data) {
			$('#answer_zone').html(data["rendered"]);
            checkNumPlayers(data);
			playSwitches();
		});
	});

	$('#likes').click(function(){
	    var title;
	    title = $(this).attr("data-title");
	    $.get('/like_statement/', {title: title}, function(data){
	               $('#like_count').html(data);
	               disableLike();
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
                playSwitches();
			});
		}
	});

	$("body").on('click', '.editable_name', function(event) {
		$(this).html("");
		$(this).attr('contenteditable', true);
		$(this).focus();
	});

});

function playSwitches() {
    $('input:checkbox').bootstrapSwitch();
    $('input:checkbox').bootstrapSwitch('onText','Yeah');
    $('input:checkbox').bootstrapSwitch('offText','Nope');
}

function disableAdd() {
    $('#add_button').prop('disabled', true);
}

function disableLike() {
    $('#likes').prop('disabled', true);
}

function checkNumPlayers(data){
    if (data["nPlayers"] >= 6){
        disableAdd();
    }
}