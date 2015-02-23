import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django

django.setup()

from neverever.models import Category, Statement, Session, Player, Answer


def populate():
    # add categories
    cat_nsfw = add_category("NSFW")
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

    state_stealing = add_statement(categories=[cat_nsfw, cat_illegal],
                     title="stolen something",
                     views=70
                     )

    state_murder = add_statement(categories=[cat_nsfw, cat_violence],
                   title="killed a person"
                   )

    add_statement(categories=[cat_nsfw, cat_alcohol],
                  title="thrown up after drinking too much",
                  views=60
    )

    add_statement(categories=[cat_nsfw, cat_alcohol, cat_illegal],
                  title="got drunk when I was underage"
    )

    add_statement(categories=[cat_nsfw, cat_sexual],
                  title="had a threesome"

    )

    state_publicsex = add_statement(categories=[cat_nsfw, cat_sexual],
                      title="Had sex in public"
                      )

    # add sessions
    session_1 = add_session(statements=[state_bungeejump, state_murder])
    session_2 = add_session(statements=[state_publicsex])
    session_3 = add_session(statements=[state_bungeejump, state_publicsex, state_murder, state_stealing, state_redlight])

    # add players
    player_1 = add_player(session=session_1)
    player_2 = add_player(session=session_1)
    player_3 = add_player(session=session_2)
    player_4 = add_player(session=session_3)
    player_5 = add_player(session=session_3)

    # add answers
    add_answer(session=session_1, statement=state_bungeejump, player=player_1, answer=True)
    add_answer(session=session_1, statement=state_murder, player=player_1, answer=False)
    add_answer(session=session_1, statement=state_bungeejump, player=player_2, answer=False)
    add_answer(session=session_2, statement=state_publicsex, player=player_3, answer=True)
    add_answer(session=session_3, statement=state_bungeejump, player=player_4, answer=False)
    add_answer(session=session_3, statement=state_publicsex, player=player_4, answer=False)
    add_answer(session=session_3, statement=state_murder, player=player_4, answer=True)
    add_answer(session=session_3, statement=state_stealing, player=player_4, answer=False)
    add_answer(session=session_3, statement=state_publicsex, player=player_5, answer=False)
    add_answer(session=session_3, statement=state_murder, player=player_5, answer=True)
    add_answer(session=session_3, statement=state_stealing, player=player_5, answer=False)
    add_answer(session=session_3, statement=state_redlight, player=player_5, answer=True)

    # Print out what we have added to the user.
    for s in Statement.objects.all():
        print "Added '{}' (Categories: ".format(str(s)),
        for cat in s.categories.all():
            print "'" + str(cat) + "' ",
        print ")"


def add_category(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

def add_statement(categories, title, views=0):
    s = Statement.objects.get_or_create(title=title, views=views)[0]
    for category in categories:
        s.categories.add(category)
    s.save()
    return s

def add_session(statements):
    s = Session.objects.get_or_create()[0]
    for statement in statements:
        s.statements.add(statement)
    s.save()
    return s

def add_player(session):
    p = Player.objects.get_or_create()[0]
    p.session.add(session)
    p.save()
    return p

def add_answer(session, statement, player, answer):
    a = Answer.objects.get_or_create()[0]
    a.session.add(session)
    a.statement.add(statement)
    a.player.add(player)
    a.save()
    return a

# Start execution here!
if __name__ == '__main__':
    print "Starting NeverHaveIEver population script..."
    populate()