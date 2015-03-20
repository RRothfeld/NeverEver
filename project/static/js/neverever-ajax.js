
$('#add_button').click(function(){
	//var sid;
	//sid = $(this).attr("data-sid");
	$.get('/add_player/', function(data) {
		$('#answer_zone').html(data);
	});
});

$('#likes').click(function(){
    var title;
    title = $(this).attr("data-title");
    $.get('/neverever/like_statement/', {title: title}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
});
