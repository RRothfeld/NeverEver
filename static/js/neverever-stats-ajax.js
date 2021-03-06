$(document).ready(function() {

    // loads relevant statement titles when a category is selected on stats page
    $("body").on('click', '.cat_list_item', function() {
        var cat_name
        cat_name = $(this).attr('data-name');
        $.get('/statement_titles/', {cat_name: cat_name}, function(data) {
            $('#statements').html(data);
        });
    });

    // loads relevant statement stats when a statement is selected on stats page
    $("body").on('click', '.single_statement', function() {
        var statement_title;
        statement_title = $(this).attr('data-title');
        $.get('/statement_info/', {title: statement_title}, function(data) {
            $('#statement_stats').html(data);
        });
    });
});