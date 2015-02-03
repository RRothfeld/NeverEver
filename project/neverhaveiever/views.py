from django.shortcuts import render

from neverhaveiever.models import Category, Statement


def index(request):

    category_list = Category.objects.order_by('-views')
    context_dict = {'categories': category_list}
    return render(request, 'neverhaveiever/index.html', context_dict)


def category(request, category_name_slug):

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
    return render(request, 'neverhaveiever/category.html', context_dict)
