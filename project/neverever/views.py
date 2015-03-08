from django.shortcuts import render

from neverever.models import Category, Statement, Session, Player, Answer,GlobalCounter
from neverever.forms import StatementForm, AnswerForm, SessionForm


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
    num_sessions = Session.objects.count()
    context_dict['nSessions'] = num_sessions
    num_players = Player.objects.count()
    context_dict['nPlayers'] = num_players
    return render(request, 'neverever/index.html', context_dict)


def about(request):
    return render(request, 'neverever/about.html')


def stats(request):
    gc = GlobalCounter.objects.all()[0]
    context_dict = {'globalCounter' : gc}
    return render(request, 'neverever/stats.html', context_dict)


def stats_options(request):
    context_dict = {}
    return render(request, 'neverever/statsOptions.html', context_dict)


def play(request):

    context_dict = {}
    sid = request.session.session_key
    SESSION_NSFW = False
    if sid:
        session = Session.objects.filter(sid=sid)
        if session:
            context_dict['session'] = "Already existed"
        else:
            context_dict['session'] = "Just created"
            s = Session.objects.get_or_create(sid=sid, nsfw=SESSION_NSFW)[0]
            for cat in Category.objects.all():
                s.categories.add(cat)
            # s.players[0] = Player.objects.get_or_create(stamp=123)  # TODO: CHANGE TO create()
            s.save()
            #manually creating players for now
            p1 = Player.objects.create(stamp=1, session=s)
            p2 = Player.objects.create(stamp=2, session=s)
            p3 = Player.objects.create(stamp=3, session=s)
            p4 = Player.objects.create(stamp=4, session=s)

            session = [s]

            # Update global counters
            gc = GlobalCounter.objects.all()[0]
            gc.total_sessions += 1
            gc.total_players += 1
            gc.save()

        categories = session[0].categories.all()
        context_dict['categories'] = categories

        while True:
            try:
                rand_cat = random.choice(categories)
                if session[0].nsfw:
                    rand_statement = random.choice(Statement.objects.filter(categories=rand_cat))
                else:
                    rand_statement = random.choice(Statement.objects.filter(categories=rand_cat, nsfw=False))
                break
            except IndexError:
                pass
        context_dict['statement'] = rand_statement

        # Testing players
        players = Player.objects.filter(session=session[0])
        context_dict['Players'] = players
    else:
        request.session.save()
        request.session.modified = True
        sid = request.session.session_key
    context_dict['sid'] = sid
    
    if request.method == 'POST':
        session = Session.objects.get(sid=sid)
        num_players = session.num_players
        forms = []
        for i in range(0, num_players):
            forms.append(AnswerForm(request.POST, prefix="form" + str(i)))

        for i in range(0, num_players):
            if forms[i].is_valid():
                answer = forms[i].save(commit = False)
                answer.statement = rand_statement
                answer.session = Session.objects.get(sid=sid)
                answer.player = players[i]  #Player.objects.get(stamp=123)
                answer.save()
            else:
                print form.errors
 
   # displays a form for each player
    else:
        session = Session.objects.get(sid=sid)
        num_players = session.num_players
        forms = []
        for i in range(0, num_players):
            forms.append(AnswerForm(prefix = "form" + str(i)))

    context_dict['forms'] = forms
    
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

    # TODO: refine it
    try:
        session[0].delete()
    except:
        response = HttpResponse("Session has ended")
    return response


# TODO: make sure that at least one Category is selected
def play_options(request):
    context_dict = {}

    try:
        sid = request.session.session_key
        session = Session.objects.get(sid=sid)
    except Session.DoesNotExist:
        return index(request)

    if request.method == 'POST':
        form = SessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save(commit=True)
            #return play(request) # <- ERROR (Sends POST request to play()
            return HttpResponseRedirect('/play')
        else:
            print form.errors
    else:
        form = SessionForm(instance=session)

    context_dict['form'] = form
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

        # TODO: MODIFY (Testing prepopulated forms)
        #u = Statement.objects.get(title="had sex in public")
        #form = StatementForm(instance=u)

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