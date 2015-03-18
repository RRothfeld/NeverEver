import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django

django.setup()

from neverever.models import Category, Statement, Session, Player, Answer, GlobalCounter, Result


def populate():

    # add global counter
    global_counter = add_global_counters(t_sessions=0, t_players=0)

    # add categories
    cat_law = add_category("Law")
    cat_drinking = add_category("Drinking")
    cat_dirty = add_category("Dirty")
    cat_love = add_category("Love")
    cat_student = add_category("#StudentLife")
    cat_work = add_category("Work")
    cat_random = add_category("Random")

    # add statements
    add_statement(categories=[cat_random],
                      title="been bungee jumping.",
                      views=10
    )

    add_statement(categories=[cat_law],
                     title="run a red light.",
                     views=130
    )

    add_statement(categories=[cat_law],
                     title="stolen something.",
                     views=70
    )

    add_statement(categories=[cat_law],
                  title="killed a person."
    )

    add_statement(categories=[cat_drinking],
                  title="thrown up after drinking too much.",
                  views=60
    )

    add_statement(categories=[cat_dirty],
                  title="watched porn with someone else.",
                  nsfw=True
    )

    add_statement(categories=[cat_dirty],
                  title="walked in on my parents having sex.",
                  nsfw=True
    )

    add_statement(categories=[cat_dirty],
                  title="had sex in front of other people.",
                  nsfw=True
    )

    add_statement(categories=[cat_dirty],
                  title="fantasised about anyone in this room.",
                  nsfw=True
    )

    add_statement(categories=[cat_dirty],
                  title="used a sex toy.",
                  nsfw=True
    )

    add_statement(categories=[cat_dirty],
                  title="had sex with someone more than 10 years older than me.",
                  nsfw=True
    )

    add_statement(categories=[cat_dirty, cat_law],
                  title="flashed someone.",
                  nsfw=True
    )

    add_statement(categories=[cat_dirty],
                  title="had anal sex.",
                  nsfw=True
    )

    add_statement(categories=[cat_dirty],
                  title="attempted anal sex and failed.",
                  nsfw=True
    )

    add_statement(categories=[cat_dirty],
                  title="slept with someone I thought was ugly.",
                  nsfw=True
    )

    add_statement(categories=[cat_drinking],
                  title="passed out from drinking.",
                  nsfw=False
    )

    add_statement(categories=[cat_law],
                  title="smoked weed.",
                  nsfw=True
    )

    add_statement(categories=[cat_random],
                  title="shot a gun.",
                  nsfw=False
    )

    add_statement(categories=[cat_random],
                  title="had surgery.",
                  nsfw=False
    )

    add_statement(categories=[cat_random],
                  title="been on TV.",
                  nsfw=False
    )

    add_statement(categories=[cat_law],
                  title="gotten into a club with fake ID.",
                  nsfw=False
    )

    add_statement(categories=[cat_random],
                  title="read the Bible.",
                  nsfw=False
    )

    add_statement(categories=[cat_random],
                  title="read the Qur'an.",
                  nsfw=False
    )

    add_statement(categories=[cat_random],
                  title="played strip poker.",
                  nsfw=False
    )

    add_statement(categories=[cat_student],
                  title="aced a test without studying.",
                  nsfw=False
    )

    add_statement(categories=[cat_random],
                  title="been in a car accident.",
                  nsfw=False
    )

    add_statement(categories=[cat_work],
                  title="badmouthed my boss.",
                  nsfw=False
    )

    add_statement(categories=[cat_work],
                  title="undeservingly gotten promoted.",
                  nsfw=False
    )

    add_statement(categories=[cat_love],
                  title="been rejected by my crush.",
                  nsfw=False
    )

    add_statement(categories=[cat_love],
                  title="had a boyfriend/girlfriend.",
                  nsfw=False
    )

    add_statement(categories=[cat_student],
                  title="cheated on an exam.",
                  nsfw=False
    )

    add_statement(categories=[cat_student],
                  title="plagiarised without getting caught.",
                  nsfw=False
    )

    state_underage_drunk = add_statement(categories=[cat_drinking, cat_law],
                                         title="got drunk when I was underage."
    )

    state_threesome = add_statement(categories=[cat_dirty],
                                    title="had a threesome.",
                                    nsfw=True
    )

    state_publicsex = add_statement(categories=[cat_dirty],
                                    title="had sex in public.",
                                    nsfw=True
    )

    # add results
    add_result(statement=state_publicsex, answer=True, gender='Male', nationality='British')
    add_result(statement=state_threesome, answer=False)
    add_result(statement=state_underage_drunk, answer=True, age=17, )

""" TO BE DELETED LATER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # add sessions
    session_1 = add_session(sid=1, categories=[cat_law])
    session_2 = add_session(sid=2, categories=[cat_law])
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