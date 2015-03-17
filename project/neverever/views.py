from django.shortcuts import render

from neverever.models import Category, Statement, Session, Player, Answer, GlobalCounter, Result
from neverever.forms import StatementForm, AnswerForm, SessionForm, PlayerForm

from django.db.models import Q


import random  # Fetch random statements


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
    results = Result.objects.all()
    context_dict = {'globalCounter': gc, 'results': results}
    return render(request, 'neverever/stats.html', context_dict)


def play(request):

    context_dict = {}
    sid = request.session.session_key
    SESSION_NSFW = False

    if not sid:
        request.session.save()
        request.session.modified = True
        return HttpResponseRedirect('/play')

    context_dict['sid'] = sid

    session_tuple = Session.objects.get_or_create(sid=sid)
    session = session_tuple[0]
    print "Session tuple[1]:", session_tuple[1]
    if not session_tuple[1]:
        context_dict['session'] = "Already existed"

    else:
        context_dict['session'] = "Just created"
        session.nsfw = SESSION_NSFW
        for cat in Category.objects.all():
            session.categories.add(cat)
        # s.players[0] = Player.objects.get_or_create(stamp=123)  # TODO: CHANGE TO create()
        session.save()
        # manually creating player 1
        p1 = Player.objects.create(stamp=1, session=session)

        # Update global counters
        gc = GlobalCounter.objects.all()[0]
        gc.total_sessions += 1
        gc.total_players += 1
        gc.save()


    print "GOT HERE: 1"
    categories = session.categories.all()
    context_dict['categories'] = categories
    print "Categories size:", len(categories)

    # Testing players
    players = Player.objects.filter(session=session)
    context_dict['Players'] = players

    if request.method == 'POST':

        # Testing
        session = Session.objects.filter(sid=sid)[0]
        used_statement = session.last_statement
        print used_statement
        session.used_statements.add(used_statement)

        session = Session.objects.get(sid=sid)
        num_players = session.num_players
        forms = []
        for i in range(0, num_players):
            forms.append(AnswerForm(request.POST, prefix="form" + str(i)))

        for i in range(0, num_players):
            if forms[i].is_valid():
                answer = forms[i].save(commit=False)
                answer.statement = used_statement
                answer.session = Session.objects.get(sid=sid)
                answer.player = players[i]  # Player.objects.get(stamp=123)
                answer.save()
            else:
                print forms[i].errors

    # displays a form for each player

    session = Session.objects.get(sid=sid)
    num_players = session.num_players
    forms = []
    for i in range(0, num_players):
        forms.append(AnswerForm(prefix="form" + str(i)))

    context_dict['forms'] = forms

    # Pick a random statement from the selected categories
    while True:
        try:
            rand_cat = random.choice(categories)
            q_object = Q(categories=categories[0])
            if len(categories) > 1:
                for category in categories[1:]:
                    q_object = q_object | Q(categories=category)
            if session.nsfw:
                statement_list = Statement.objects.filter(q_object).order_by('?')
            else:
                statement_list = Statement.objects.filter(q_object, nsfw=False).order_by('?')
            print "Statements Size:", len(statement_list)
            found = False
            rand_statement = None
            for statement in statement_list:
                if statement not in session.used_statements.all():
                    rand_statement = statement
                    found = True
                    break
            print "FOUND:", found, "ITEM LIST SIZE:", len(session.used_statements.all())
            if not found:
                context_dict["no_more_statements"] = True
            # if session.nsfw:
            #     rand_statement = random.choice(Statement.objects.filter(categories=rand_cat))
            # else:
            #     rand_statement = random.choice(Statement.objects.filter(categories=rand_cat, nsfw=False))
            # if rand_statement in session.used_statements.all():
            #     print "STATEMENT HAS BEEN SELECTED IN THE PAST"
            #     continue
            break
        except SyntaxError as e:
            print e.message

    context_dict['statement'] = rand_statement

    # Testing
    session.last_statement = rand_statement
    session.save()
    
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

    if request.method == 'POST':
        # this is where we put things if the form has been submitted

        session = Session.objects.get(sid=sid)
        num_players = session.num_players
        forms = []
        for i in range(0, num_players):
            count = 1
            p = Player.objects.get(stamp=count)  # TODO change so different player
            forms.append(PlayerForm(request.POST, prefix="form" + str(i), instance=p))
            count = count+1

        for i in range(0, num_players):
            if forms[i].is_valid():
                player = forms[i].save(commit=False)
                # note need to make sure is saving their details here
                # player.stamp =
                player.session = Session.objects.get(sid=sid)
                player.save()
            else:
                print forms[i].errors
    else:
        # display the forms for each user
        session = Session.objects.get(sid=sid)
        num_players = session.num_players
        forms = []
        for i in range(0, num_players):
            forms.append(PlayerForm(prefix="form" + str(i)))

    context_dict['forms'] = forms

    players = Player.objects.filter(session=session).order_by('id')
    print "len(players):", len(players)

    player_answers = []
    for player in players:
        print 1
        player_answers.append(Answer.objects.filter(player=player))
        print "player_answers[-1]:", len(player_answers[-1])

    context_dict['player_answers'] = player_answers

    response = render(request, 'neverever/playSummary.html', context_dict)
    return response



    # TODO: refine it
    # try:
    #     session[0].delete()
    # except:
    #     response = HttpResponse("Session has ended")
    # return response


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
            s = form.save(commit=True)
            num_players = s.num_players
            for i in range(1, num_players+1):
                Player.objects.get_or_create(stamp=i, session = session)

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