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
        cat_name = $(this).html();
        $.get('/stats_test/', {cat_name: cat_name}, function(data) {
            $('#statements').html(data);
        });
    });
});