import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django

django.setup()

from neverever.models import Category, Statement, Session, Player, Answer, GlobalCounter, Result


def populate():

    # add global counter
    global_counter = add_global_counters(t_sessions=0, t_players=0)

    # add categories
    cat_violence = add_category("Violence")
    cat_illegal = add_category("Illegal")
    cat_alcohol = add_category("Alcohol")
    cat_sexual = add_category("Sexual")
    cat_activity = add_category("Activities")

    # add statements
    state_bungeejump = add_statement(categories=[cat_activity],
                      title="been bungee jumping",
                      views=10,
                      )

    state_redlight = add_statement(categories=[cat_illegal],
                     title="run a red light",
                     views=130,
                     )

    state_stealing = add_statement(categories=[cat_illegal],
                     title="stolen something",
                     views=70
                     )

    state_murder = add_statement(categories=[cat_violence],
                                 title="killed a person"
    )

    add_statement(categories=[cat_alcohol],
                  title="thrown up after drinking too much",
                  views=60
    )

    state_underage_drunk = add_statement(categories=[cat_alcohol, cat_illegal],
                                         title="got drunk when I was underage"
    )

    state_threesome = add_statement(categories=[cat_sexual],
                                    title="had a threesome",
                                    nsfw=True
    )

    state_publicsex = add_statement(categories=[cat_sexual],
                                    title="had sex in public",
                                    nsfw=True
    )

    # add results
    add_result(statement=state_publicsex, answer=True, gender='Male', nationality='British')
    add_result(statement=state_threesome, answer=False)
    add_result(statement=state_underage_drunk, answer=True, age=17, )

"""
    # add sessions
    session_1 = add_session(sid=1, categories=[cat_violence])
    session_2 = add_session(sid=2, categories=[cat_illegal])
    session_3 = add_session(sid=3, categories=[cat_alcohol, cat_sexual, cat_activity])

    # add players
    player_1 = add_player(stamp=1)
    player_2 = add_player(stamp=2)
    player_3 = add_player(stamp=3)
    player_4 = add_player(stamp=4)
    player_5 = add_player(stamp=5)

    # add answers
    add_answer(stamp=1, session=session_1, statement=state_bungeejump, player=player_1, answer=True)
    add_answer(stamp=2, session=session_1, statement=state_murder, player=player_1, answer=False)
    add_answer(stamp=3, session=session_1, statement=state_bungeejump, player=player_2, answer=False)
    add_answer(stamp=4, session=session_2, statement=state_publicsex, player=player_3, answer=True)
    add_answer(stamp=5, session=session_3, statement=state_bungeejump, player=player_4, answer=False)
    add_answer(stamp=6, session=session_3, statement=state_publicsex, player=player_4, answer=False)
    add_answer(stamp=7, session=session_3, statement=state_murder, player=player_4, answer=True)
    add_answer(stamp=8, session=session_3, statement=state_stealing, player=player_4, answer=False)
    add_answer(stamp=9, session=session_3, statement=state_publicsex, player=player_5, answer=False)
    add_answer(stamp=10, session=session_3, statement=state_murder, player=player_5, answer=True)
    add_answer(stamp=11, session=session_3, statement=state_stealing, player=player_5, answer=False)
    add_answer(stamp=12, session=session_3, statement=state_redlight, player=player_5, answer=True)
"""

def add_category(name):
    c = Category.objects.get_or_create(name=name)[0]
    print "Adding category " + str(name)
    return c

def add_statement(categories, title, views=0, nsfw=False):
    s = Statement.objects.get_or_create(title=title, views=views, nsfw=nsfw)[0]
    for category in categories:
        s.categories.add(category)
    s.save()
    print "Adding statement " + str(title)
    return s

def add_session(sid, categories):
    s = Session.objects.get_or_create(sid=sid)[0]
    for category in categories:
        s.categories.add(category)
    s.save()
    print "Adding session " + str(s.sid)
    return s

def add_player(stamp):
    p = Player.objects.get_or_create(stamp=stamp)[0]
    p.save()
    print "Adding player " + str(p.stamp)
    return p

def add_answer(stamp, session, statement, player, answer):
    a = Answer.objects.get_or_create(stamp=stamp)[0]
    a.session = session
    a.statement = statement
    a.player = player
    a.answer = answer
    a.save()
    print "Adding answer " + str(a.stamp)
    return a

def add_global_counters(t_sessions, t_players):
    gc = GlobalCounter.objects.create(total_sessions=t_sessions, total_players=t_players)
    print "Adding global counter " + str(gc)
    return gc

def add_result(statement, answer, gender=None, nationality=None, age=None):
    result = Result.objects.create(statement=statement, answer=answer, gender=gender, nationality=nationality,
                                   age=age)
    print "Adding result " + str(result)
    return result

# Start execution here!
if __name__ == '__main__':
    print "Starting NeverHaveIEver population script..."
    populate()
    print "Population successful."