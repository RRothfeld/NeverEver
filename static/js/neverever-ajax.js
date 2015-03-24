$(document).ready(function(data) {

    if ($('#No-statement').length){
        disableLike();
        disableAdd();
    }

    // check number of players in the game (max 6)
    $.get('/get_game_data/', function(data) {
        checkNumPlayers(data);
    });

    // enable animated switches
    playSwitches();

	// add a new player to the game on clicking add player button
	$('#add_button').click(function(){
		$.get('/add_player/', function(data) {
			$('#answer_zone').html(data["rendered"]);
            checkNumPlayers(data);
			playSwitches();
		});
	});

	// increment likes for the statement on clicking like button
	$('#likes').click(function(){
	    var title;
	    title = $(this).attr("data-title");
	    $.get('/like_statement/', {title: title}, function(data){
	               $('#like_count').html(data);
	               disableLike();
	    });
	});

	// initialise popover when page is loaded
	$(function() {
		$("[data-toggle='popover']").popover();
	});
	
	// reinitalise popover after ajax content is loaded
	$(document).ajaxComplete(function() {
		$(function() {
			$("[data-toggle='popover']").popover();
		});
	});

	// save name entered by user and reload relevant part of page
	// triggered when user presses enter key
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

	// make name editable upon clicking so that player can enter his name
	$("body").on('click', '.editable_name', function(event) {
		$(this).html("");
		$(this).attr('contenteditable', true);
		$(this).focus();
	});

});

// helper function to set up the answer buttons
function playSwitches() {
    $('input:checkbox').bootstrapSwitch();
    $('input:checkbox').bootstrapSwitch('onText','Yeah');
    $('input:checkbox').bootstrapSwitch('offText','Nope');
}

// helper function to disable the add player button
function disableAdd() {
    $('#add_button').prop('disabled', true);
}

// helper function to disable the like button
function disableLike() {
    $('#likes').prop('disabled', true);
}

// disable add player button if number of players in game gets to 6
function checkNumPlayers(data){
    if (data["nPlayers"] >= 6){
        disableAdd();
    }
}