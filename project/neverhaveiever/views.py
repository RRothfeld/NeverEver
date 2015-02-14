from django.shortcuts import render

from neverhaveiever.models import Category, Statement


def index(request):

    context_dict = {}
    return render(request, 'neverhaveiever/index.html', context_dict)


def about(request):
    return render(request, 'neverhaveiever/about.html')


def stats(request):
    context_dict = {}
    return render(request, 'neverhaveiever/stats.html', context_dict)


def stats_options(request):
    context_dict = {}
    return render(request, 'neverhaveiever/statsOptions.html', context_dict)


def play(request):
    context_dict = {}
    return render(request, 'neverhaveiever/play.html', context_dict)

def play_summary(request):
    context_dict = {}
    return render(request, 'neverhaveiever/playSummary.html', context_dict)

def play_options(request):
    context_dict = {}
    return render(request, 'neverhaveiever/playOptions.html', context_dict)

def new_statement(request):
    context_dict = {}
    return render(request, 'neverhaveiever/newStatement.html', context_dict)


#TODO:Remove
def testing(request):
    category_list = Category.objects.order_by('name')
    context_dict = {'categories': category_list}
    return render(request, 'neverhaveiever/testing.html', context_dict)

def testing_category(request, category_name_slug):

    context_dict = {}
    try:
        selected_category = Category.objects.get(slug=category_name_slug)
        statements = Statement.objects.filter(category=selected_category)

        context_dict['category_name'] = selected_category.name
        context_dict['statements'] = statements

        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = selected_category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'neverhaveiever/testingCategories.html', context_dict)