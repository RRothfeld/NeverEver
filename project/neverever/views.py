from django.shortcuts import render

from neverever.models import Category, Statement, Session, Player, Answer
from neverever.forms import StatementForm


import random # Fetch random statements


# TODO: fix duplicate code in play and index (detect sid)


def index(request):

    context_dict = {}
    sid = request.session.session_key
    if not sid:
        request.session.save()
        request.session.modified = True
        sid = request.session.session_key
    context_dict['sid'] = sid
    return render(request, 'neverever/index.html', context_dict)


def about(request):
    return render(request, 'neverever/about.html')


def stats(request):
    context_dict = {}
    return render(request, 'neverever/stats.html', context_dict)


def stats_options(request):
    context_dict = {}
    return render(request, 'neverever/statsOptions.html', context_dict)


def play(request):

    context_dict = {}
    sid = request.session.session_key
    if sid:
        session = Session.objects.filter(sid=sid)
        if session:
            context_dict['session'] = "Already existed"
        else:
            context_dict['session'] = "Just created"
            s = Session.objects.get_or_create(sid=sid)[0]
            for cat in Category.objects.all():
                s.categories.add(cat)
            s.save()
            session = [s]
        categories = session[0].categories.all()
        context_dict['categories'] = categories
        rand_cat = random.choice(categories)
        rand_statement = random.choice(Statement.objects.filter(categories=rand_cat))
        context_dict['statement'] = rand_statement
    else:
        request.session.save()
        request.session.modified = True
        sid = request.session.session_key
    context_dict['sid'] = sid
    response = render(request, 'neverever/play.html', context_dict)
    return response


def play_summary(request):
    context_dict = {}
    sid = request.session.session_key
    if sid:
        session = Session.objects.filter(sid=sid)
        if session:
            context_dict['session'] = session[0]
    else:
        request.session.save()
        request.session.modified = True
        sid = request.session.session_key
    context_dict['sid'] = sid

    response = render(request, 'neverever/playSummary.html', context_dict)
    session[0].delete()
    return response


# TODO: make sure that at least one Category is selected
def play_options(request):
    context_dict = {}
    return render(request, 'neverever/playOptions.html', context_dict)


# TODO: Remove
from django.http import HttpResponseRedirect, HttpResponse


def new_statement(request):
    context_dict = {}

    if request.method=='POST':
        form = StatementForm(request.POST)
        if form.is_valid():
            statement = form.save(commit=False)
            # if 'categories' in request.POST.keys():
            #    for
            # statement.save()
            # return HttpResponseRedirect(request)
            s = ""
            statement.save()
            for k in form.cleaned_data['categories']:
                statement.categories.add(Category.objects.filter(id=k)[0])
            statement.save()
            return HttpResponseRedirect('/')
        else:
            print form.errors
    else:
        form = StatementForm()
    return render(request, 'neverever/newStatement.html', {'form': form})



#TODO:Remove
def testing(request):
    category_list = Category.objects.order_by('name')
    context_dict = {'categories': category_list}
    return render(request, 'neverever/testing.html', context_dict)

def testing_category(request, category_name_slug):

    context_dict = {}
    try:
        selected_category = Category.objects.get(slug=category_name_slug)
        statements = Statement.objects.filter(categories=selected_category)

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
    return render(request, 'neverever/testingCategories.html', context_dict)