$(document).ready(function() {
        /*$('.menu > li').mouseover(function() {
            //alert("bla");
            $(this).find('ul').css('visibility', 'visible');
        });*/

    $("body").on('mouseover', '#catlist', function() {
        //alert("bla");
        $(this).find('ul').css('visibility', 'visible');
    });

    $("body").on('mouseout', '.menu > li', function() {
        $(this).find('ul').css('visibility', 'hidden');
    });

    /*$('.cat_list_item').click(function() {
        var cat_name
        cat_name = $(this).html();
        $.get('/stats_test/', {cat_name: cat_name}, function(data) {
            $("body").html(data);
        });
    });*/

    $("body").on('click', '.cat_list_item', function() {
        //alert("come on");
        var cat_name
        cat_name = $(this).attr('data-name');
        $.get('/stats_test/', {cat_name: cat_name}, function(data) {
            $('#statements').html(data);
        });
    });

    $("body").on('click', '.single_statement', function() {
        //alert("hey there")
        var statement_title;
        statement_title = $(this).attr('data-title');
        $.get('/statement_info/', {title: statement_title}, function(data) {
            $('#statement_stats').html(data);
        });
    });
});