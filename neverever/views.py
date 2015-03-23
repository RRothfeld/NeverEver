from django.shortcuts import render

from neverever.models import Category, Statement, Session, Player, Answer, GlobalCounter, Result
from neverever.forms import StatementForm, AnswerForm, SessionForm, PlayerForm

import json
from django.template.loader import render_to_string
from django.template import RequestContext
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse

from collections import Counter


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


def update_count(request):
    context_dict = {}
    num_sessions = Session.objects.count()
    context_dict['nSessions'] = num_sessions
    num_players = Player.objects.count()
    context_dict['nPlayers'] = num_players
    return render(request, 'neverever/sessionFooter.html', context_dict)


def about(request):
    return render(request, 'neverever/about.html')


def stats(request):
    gc = GlobalCounter.objects.all()[0]
    results = Result.objects.all()
    context_dict = {'globalCounter': gc, 'results': results}

    statements_list = []

    statements = Statement.objects.all()
    for statement in statements:
        yes = 0
        no = 0

        statement_answers = Result.objects.filter(statement=statement)
        # print len(statement_answers)
        for result in statement_answers:
            if result.answer:
                yes += 1
            else:
                no += 1
        total = yes+no
        if total > 0:
            yes_percentage = (yes*100/total)
            no_percentage = (no*100/total)
        else:
            yes_percentage = False
            no_percentage = False
        statements_list.append({'title': statement, "yes": yes, "no": no, "total": total,
                                "yes_percentage": yes_percentage, "no_percentage": no_percentage})

    context_dict['statements'] = statements_list
    categories = Category.objects.all();
    context_dict['categories'] = categories
    return render(request, 'neverever/stats.html', context_dict)

def stats_test(request):
    if request.method == 'GET':
        cat_name = request.GET['cat_name']
        print cat_name

    category = Category.objects.get(name=cat_name)

    statements = Statement.objects.filter(categories=category)

    return render(request, 'neverever/statementTitles.html', {'statements': statements})


def statement_info(request):
    
    nats = ('mexican', 'mexican', 'mexican', 'spanish', 'american', 'spanish', 'greek', 'spanish', 'mexican', 'spanish')
    print nats
    c = Counter(nats)
    common = c.most_common(2)
    print common[0][0]

    statement_title = ""
    if request.method == 'GET':
        statement_title = request.GET['title']

    statement = Statement.objects.get(title=statement_title)
    print statement

    yes = 0
    no = 0
    print statement
    female_yes = 0
    male_yes = 0

    statement_answers = Result.objects.filter(statement=statement)
    yes_nationalities = []
    
    print "got to start of loop"
    for result in statement_answers:
        if result.answer:
            yes += 1
            yes_nationalities.append(result.nationality)
            if(result.gender == 'f'):
                female_yes += 1
            elif(result.gender == 'm'):
                male_yes += 1
        else:
            no += 1
    
    total = yes+no
    female_percentage = 0
    male_percentage = 0
    if total > 0:
        yes_percentage = (yes*100/total)
        no_percentage = (no*100/total)
    else:
        yes_percentage = False
        no_percentage = False
    if yes > 0:
        female_percentage = (female_yes*100/yes)
        male_percentage = (male_yes*100/yes)

    nat_freqs = Counter(yes_nationalities).most_common()

    context_dict = {}
    context_dict['title'] = statement
    context_dict['yes'] = yes
    context_dict['no'] = no
    context_dict['total'] = total
    context_dict['yes_percentage'] = yes_percentage
    context_dict['no_percentage'] = no_percentage
    context_dict['nat_freqs'] = nat_freqs
    context_dict['female_percentage'] = female_percentage
    context_dict['male_percentage'] = male_percentage

    return render(request, 'neverever/statementStats.html', context_dict)




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

    print "SESSION last_modified:", session.last_modified
    categories = session.categories.all()
    context_dict['categories'] = categories

    # Testing players
    players = Player.objects.filter(session=session)
    context_dict['Players'] = players

    if request.method == 'POST':

        # Testing
        session = Session.objects.filter(sid=sid)[0]
        used_statement = session.last_statement
        session.used_statements.add(used_statement)

        session = Session.objects.get(sid=sid)
        num_players = len(Player.objects.filter(session=session))
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
    num_players = len(Player.objects.filter(session=session))
    forms = []
    for i in range(0, num_players):
        forms.append(AnswerForm(prefix="form" + str(i)))

    #context_dict['forms'] = forms
    #context_dict['players'] = Player.objects.all()
    players = Player.objects.filter(session = session)
    formlist = zip(forms, players)
    context_dict['formlist'] = formlist
    #context_dict['range'] = range(num_players)

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
            found = False
            rand_statement = None
            for statement in statement_list:
                if statement not in session.used_statements.all():
                    rand_statement = statement
                    found = True
                    break
            if not found:
                context_dict["no_more_statements"] = True
            break
        except SyntaxError as e:
            print e.message

    context_dict['statement'] = rand_statement

    # Testing
    session.last_statement = rand_statement
    session.save()
    # TESTING
    context_dict['this_session'] = session

    context_dict["nPlayers"] = num_players
    
    response = render(request, 'neverever/play.html', context_dict)
    return response


def like_statement(request):
    print "getting to the top of the like statement function"
    title = None
    if request.method == 'GET':
        title = request.GET['title']
    print title
    likes = 0
    if title:
        statement = Statement.objects.get(title=title)
        if statement:
            likes = statement.likes+1
            statement.likes = likes
            print statement.likes
            statement.save()

    return HttpResponse(likes)


def set_name(request):
    name = request.GET['name']
    num = request.GET['stamp']
    sid = request.session.session_key
    session = Session.objects.get(sid=sid)
    #pass it both stamp and session to make sure its the right player
    player = Player.objects.get(stamp=num, session=session)
    player.name = name
    player.save()

    num_players = len(Player.objects.filter(session=session))
    forms = []
    for i in range(0, num_players):
        forms.append(AnswerForm(prefix="form" + str(i)))

    players = Player.objects.filter(session = session)
    formlist = zip(forms, players)

    return render(request, 'neverever/answerButtons.html', {'formlist': formlist})


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
        num_players = len(Player.objects.filter(session=session))
        forms = []
        print num_players
        for i in range(0, num_players):
            #count = 1
            p = Player.objects.get(stamp=i+1, session=session)  # TODO change so different player
            forms.append(PlayerForm(request.POST, prefix="form" + str(i), instance=p))
            #count = count+1

        for i in range(0, num_players):
            if forms[i].is_valid():
                player = forms[i].save(commit=False)
                # note need to make sure is saving their details here
                # player.stamp =
                player.session = Session.objects.get(sid=sid)
                player.save()
            else:
                print forms[i].errors


        # update the response model
        responses = Answer.objects.all()
        for answer in responses:
            s = Session.objects.get(sid=sid)
            if answer.session == s:
                statement = answer.statement
                ans = answer.answer
                gender = answer.player.gender
                nationality = answer.player.nationality
                age = answer.player.age
                #use create not get_or_create as results don't have to be unique
                result = Result.objects.create(statement=statement, answer=ans, gender=gender,
                                                      nationality=nationality, age=age)
                print "getting to saving response"

        # end session
        try:
            s = Session.objects.get(sid=sid)
            s.delete()
            return HttpResponseRedirect('/')
            #response = HttpResponse("Session has ended")
        except:
            response = HttpResponse("Something went wrong. Probably ending the session")
        return response

    else:
        #display the forms for each user
        session = Session.objects.get(sid=sid)
        num_players = len(Player.objects.filter(session=session))
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
            return HttpResponseRedirect('/play')
        else:
            print form.errors
    else:
        form = SessionForm(instance=session)

    context_dict['form'] = form
    return render(request, 'neverever/playOptions.html', context_dict)


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


def add_player(request):
    sid = request.session.session_key
    players = 0
    if not sid:
        request.session.save()
        request.session.modified = True
        return HttpResponseRedirect('/play')
    session = Session.objects.get(sid=sid)
    if session:
        players = Player.objects.filter(session=session)
        session.save()
        #create more players
        print "NEW PLAYER:", (len(players) + 1)
        Player.objects.create(stamp=(len(players) + 1), session = session)

    forms = []
    session = Session.objects.get(sid=(sid))

    for i in range(0, len(players)+1):  # +1 since a new player was added
        forms.append(AnswerForm(prefix="form" + str(i)))

    players = Player.objects.filter(session = session)
    formlist = zip(forms, players)

    rendered = str(render_to_string('neverever/answerButtons.html',
                                    {'formlist': formlist},
                                    context_instance=RequestContext(request)))

    response = HttpResponse(json.dumps({'rendered': rendered, "nPlayers": len(players)}), content_type="application/json")

    return response
