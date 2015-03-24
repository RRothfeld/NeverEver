from django.shortcuts import render

from neverever.models import Category, Statement, Session, Player, Answer, GlobalCounter, Result
from neverever.forms import StatementForm, AnswerForm, SessionForm, PlayerForm

import json
from django.template.loader import render_to_string
from django.template import RequestContext
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse

from collections import Counter
from operator import itemgetter

import random  # Fetch random statements


# view for the home page
def index(request):
    return render(request, 'neverever/index.html')

# view for updating the global session and player count on home page
# called by AJAX script 
def update_count(request):
    context_dict = {}
    # get info on current number of games and players to pass to template
    num_sessions = Session.objects.count()
    context_dict['nSessions'] = num_sessions
    num_players = Player.objects.count()
    context_dict['nPlayers'] = num_players
    return render(request, 'neverever/indexFooter.html', context_dict)

# display about page
def about(request):
    return render(request, 'neverever/about.html')

# display overall stats page
def stats(request):
    # get info on total games and players
    gc = GlobalCounter.objects.all()[0]
    results = Result.objects.all()
    context_dict = {'globalCounter': gc, 'results': results}
    # get info on number of categories, statements and answers
    context_dict['nCategories'] = len(Category.objects.all())
    context_dict['nStatements'] = len(Statement.objects.all())
    context_dict['nAnswers'] = len(Answer.objects.all()) + len(Result.objects.all())
    # get list of categories to use in template
    categories = Category.objects.all();
    context_dict['categories'] = categories
    return render(request, 'neverever/stats.html', context_dict)

# display statements within chosen category on overall stats page
# (called using AJAX)
def statement_titles(request):
    if request.method == 'GET':
        # get category name received from AJAX get request
        cat_name = request.GET['cat_name']

    category = Category.objects.get(name=cat_name)
    # get list of statements in that category
    statements = Statement.objects.filter(categories=category)
    return render(request, 'neverever/statementTitles.html', {'statements': statements})

# display statistics on an individual statement on overall stats page
# (called using AJAX)
def statement_info(request):
    statement_title = ""
    if request.method == 'GET':
        # get statement title received from AJAX get request
        statement_title = request.GET['title']

    statement = Statement.objects.get(title=statement_title)
    # set up stats variables
    yes = 0
    no = 0
    female_yes = 0
    male_yes = 0
    female_percentage = 0
    male_percentage = 0
    yes_age=0
    no_age=0
    avg_yes_age=0
    avg_no_age=0
    yes_nationalities = []
    #get list of answers for this statement
    statement_answers = Result.objects.filter(statement=statement)
    for result in statement_answers:
        # if answer is yes
        if result.answer:
            yes += 1
            # if player provided their age
            if result.age:
                yes_age += result.age
            # add player nationality to list of nationalities
            yes_nationalities.append(result.nationality)
            # increment female and male yes counts
            if(result.gender == 'F'):
                female_yes += 1
            elif(result.gender == 'M'):
                male_yes += 1
        # if answer is no
        else:
            no += 1
            # if player provided their age
            if result.age:
                no_age += result.age

    total = yes+no
    # if this statement has answers, calculate yes and no percentages
    if total > 0:
        yes_percentage = (yes*100/total)
        no_percentage = (no*100/total)
    else:
        yes_percentage = False
        no_percentage = False
    
    # if this statement has yes answers, calculate female and male percentages for yes answers
    if yes > 0:
        female_percentage = (female_yes*100/yes)
        male_percentage = (male_yes*100/yes)
        avg_yes_age = yes_age/yes
    if no > 0:
        avg_no_age = no_age/no

    # get frequencies for nationalities who said yes
    nat_freqs = Counter(yes_nationalities).most_common()

    # set up context_dict to pass to template
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
    context_dict['avg_yes_age'] = avg_yes_age
    context_dict['avg_no_age'] = avg_no_age

    return render(request, 'neverever/statementStats.html', context_dict)

# display the gameplay page
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
        # if session is new, set up session
        context_dict['session'] = "Just created"
        session.nsfw = SESSION_NSFW
        for cat in Category.objects.all():
            session.categories.add(cat)

        session.save()
        # manually create player 1
        p1 = Player.objects.create(stamp=1, session=session)

        # Update global counters
        gc = GlobalCounter.objects.all()[0]
        gc.total_sessions += 1
        print "adding to total sessions"
        gc.total_players += 1
        gc.save()

    print "SESSION last_modified:", session.last_modified
    categories = session.categories.all()
    #context_dict['categories'] = categories

    # Testing players
    players = Player.objects.filter(session=session)
    #context_dict['Players'] = players

    # if we get answers back from the client
    if request.method == 'POST':
        session = Session.objects.get(sid=sid)
        # get statement that has just been answered
        used_statement = session.last_statement
        session.used_statements.add(used_statement)
        
        # get number of players in this game
        num_players = len(Player.objects.filter(session=session))
        forms = []
        # get answer forms for each player
        for i in range(0, num_players):
            forms.append(AnswerForm(request.POST, prefix="form" + str(i)))

        #loop through answer forms, give answers remaining information and save
        for i in range(0, num_players):
            if forms[i].is_valid():
                answer = forms[i].save(commit=False)
                answer.statement = used_statement
                answer.session = session
                answer.player = players[i] 
                answer.save()
            else:
                print forms[i].errors

    # Pick a random statement from the selected categories
    while True:
        try:
            random.choice(categories)
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

                    # increment view counter
                    views = statement.views+1
                    statement.views = views
                    statement.save()

                    # present found statement
                    found = True
                    break
            if not found:
                context_dict["no_more_statements"] = True
            break
        except SyntaxError as e:
            print e.message

    context_dict['statement'] = rand_statement

    # save statement to be used in this round as the last statement
    session.last_statement = rand_statement
    session.save()
    # put session in context_dict to pass to template
    context_dict['this_session'] = session
    
    response = render(request, 'neverever/play.html', context_dict)
    return response

# display the number of likes for a statement on the gameplay page
def like_statement(request):
    title = None
    if request.method == 'GET':
        # get statement title received from AJAX get request
        title = request.GET['title']

    likes = 0
    if title:
        # get statement object from title
        statement = Statement.objects.get(title=title)
        if statement:
            # increment likes and save
            likes = statement.likes+1
            statement.likes = likes
            statement.save()

    return HttpResponse(likes)

# view to save names entered by the players on the gameplay page
# and display the updated page using AJAX
def set_name(request):
    name = None
    title = None
    if request.method == 'GET':
        # get player's new name and player number from AJAX get request
        name = request.GET['name']
        num = request.GET['stamp']
    
    sid = request.session.session_key
    session = Session.objects.get(sid=sid)
    
    if name:
        #pass it both stamp and session to make sure its the right player and save their name
        player = Player.objects.get(stamp=num, session=session)
        player.name = name
        player.save()

    formlist = get_answer_forms(session)

    return render(request, 'neverever/answerButtons.html', {'formlist': formlist})

# display the end of game summary page
# we get information on the players then store this info
# along with info on the respective answers in a results model
# the rest of the data is deleted (session, players, answers) after the game is finished
def play_summary(request):
    context_dict = {}
    sid = request.session.session_key
    if sid:
        session = Session.objects.get(sid=sid)
    else:
        request.session.save()
        request.session.modified = True
        sid = request.session.session_key
        session = Session.objects.get(sid=sid)
    
    # if we are getting the player forms back from the client
    if request.method == 'POST':
        num_players = len(Player.objects.filter(session=session))
        forms = []
        # loop through forms and put in list
        for i in range(0, num_players):
            p = Player.objects.get(stamp=i+1, session=session)  # TODO change so different player
            forms.append(PlayerForm(request.POST, prefix="form" + str(i), instance=p))

        # loop through player forms and save each player object
        for i in range(0, num_players):
            if forms[i].is_valid():
                player = forms[i].save(commit=False)
                player.session = session
                player.save()
            else:
                print forms[i].errors

        # get answers belonging to this session
        responses = Answer.objects.filter(session=session)
        # go through each answer and extract relevant information, then make new result object with that info
        for answer in responses:
            statement = answer.statement
            ans = answer.answer
            gender = answer.player.gender
            nationality = answer.player.nationality
            age = answer.player.age
            #use create not get_or_create as results don't have to be unique
            result = Result.objects.create(statement=statement, answer=ans, gender=gender,
                                                  nationality=nationality, age=age)

        # delete session
        try:
            session.delete()
            return HttpResponseRedirect('/')
        except:
            response = HttpResponse("Something went wrong. Probably ending the session")
        return response

    # else if request is GET
    else:
        #display the forms for each player
        num_players = len(Player.objects.filter(session=session))
        forms = []
        player_names = []
        for i in range(0, num_players):
            forms.append(PlayerForm(prefix="form" + str(i)))
            player = Player.objects.get(stamp=i+1, session=session)
            if player.name:
                player_names.append(player.name)
            else:
                player_names.append("Player " + str(player.stamp))

    context_dict['player_forms'] = zip(player_names, forms)

    players = Player.objects.filter(session=session)
    player_answers = []
    player_total_yes_no = []
    # get answers stats for each player
    for player in players:
        player_answers.append(Answer.objects.filter(player=player))

        total_yes = Answer.objects.filter(player=player, answer=True).count()
        total_no = Answer.objects.filter(player=player, answer=False).count()
        player_total_yes_no.append({'player': player,
                                    'total_yes': total_yes,
                                    'total_no': total_no,
                                    'total': total_yes + total_no})

    player_total_yes_no = sorted(player_total_yes_no, key=itemgetter('total_yes'), reverse=True)
    # put stats in  context_dict to pass to template
    context_dict['player_answers'] = player_answers
    context_dict['player_total_yes_no'] = player_total_yes_no

    statements = session.used_statements.all()
    statement_data = []
    # get answer stats for each statement
    for statement in statements:
        answers = Answer.objects.filter(session=session, statement=statement).order_by('player__stamp')
        count_yes = answers.filter(answer=True).count()
        count_no = answers.filter(answer=False).count()
        count_total = len(answers)

        total_yes = len(Result.objects.filter(statement=statement, answer=True))
        total_yes += len(Answer.objects.filter(statement=statement, answer=True))

        total_no = len(Result.objects.filter(statement=statement, answer=False))
        total_no += len(Answer.objects.filter(statement=statement, answer=False))

        data = {'yes':count_yes,
                'no': count_no,
                'total': count_total,
                'answers': answers}
        statement_data.append((statement, data, total_yes, total_no))

    # put stats in context_dict to pass to template
    context_dict['statement_data'] = statement_data
    response = render(request, 'neverever/playSummary.html', context_dict)
    return response

# display the options page
def play_options(request):
    context_dict = {}

    try:
        sid = request.session.session_key
        session = Session.objects.get(sid=sid)
    except Session.DoesNotExist:
        return index(request)

    if request.method == 'POST':
        # save session form obtained from options page with session categories
        form = SessionForm(request.POST, instance=session)
        if form.is_valid():
            s = form.save(commit=True)
            return HttpResponseRedirect('/play')
        else:
            print form.errors
    # else, if GET request
    else:
        form = SessionForm(instance=session)

    context_dict['form'] = form
    return render(request, 'neverever/playOptions.html', context_dict)

# display page to add new statement
def new_statement(request):
    context_dict = {}

    if request.method=='POST':
        # save statement form obtained from new statement page
        form = StatementForm(request.POST)
        if form.is_valid():
            statement = form.save(commit=False)
            statement.save()
            for k in form.cleaned_data['categories']:
                statement.categories.add(Category.objects.filter(id=k)[0])
            statement.save()
            return HttpResponseRedirect('/')
        else:
            print form.errors
    # else, if GET request
    else:
        form = StatementForm()

    return render(request, 'neverever/newStatement.html', {'form': form})

# view to add a player during game and display the updated page using AJAX
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
        # create new player in this session
        Player.objects.create(stamp=(len(players) + 1), session = session)
        # update global player counter
        gc = GlobalCounter.objects.all()[0]
        gc.total_players += 1
        gc.save()

    formlist = get_answer_forms(session)
    # rendering the answer buttons template and context to load within gameplay page
    rendered = str(render_to_string('neverever/answerButtons.html',
                                    {'formlist': formlist},
                                    context_instance=RequestContext(request)))

    response = HttpResponse(json.dumps({'rendered': rendered, "nPlayers": len(players)+1}),
                            content_type="application/json")

    return response


def get_game_data(request):
    sid = request.session.session_key
    session = Session.objects.get(sid=sid)
    num_players = len(Player.objects.filter(session=session))
    return HttpResponse(json.dumps({'nPlayers': num_players}), content_type="application/json")

def get_answer_forms(session):
    # get list of players
    players = Player.objects.filter(session = session)
    forms = []
    # add a form for each player to list of forms
    for i in range(0, len(players)): 
        forms.append(AnswerForm(prefix="form" + str(i)))
    # zip list of forms and players so that we can loop through both in the template   
    formlist = zip(forms, players)
    return formlist

