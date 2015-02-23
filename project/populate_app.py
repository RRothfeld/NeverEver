import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django

django.setup()

from neverever.models import Category, Statement, Session, Player, Anwser


def populate():
    # add categories
    cat_nsfw = add_category("NSFW")
    cat_violence = add_category("Violence")
    cat_illegal = add_category("Illegal")
    cat_alcohol = add_category("Alcohol")
    cat_sexual = add_category("Sexual")
    cat_activity = add_category("Activities")

    # add statements
    state_bungejump = add_statement(categories=[cat_activity],
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
    session_1 = add_session(statements=[state_bungejump, state_murder])
    session_2 = add_session(statements=[state_publicsex])
    session_3 = add_session(statements=[state_bungejump, state_publicsex, state_murder, state_stealing, state_redlight])

    # add players
    player_1 = add_player(session_1)
    player_2 = add_player(session_1)
    player_3 = add_player(session_2)
    player_4 = add_player(session_3)
    player_5 = add_player(session_3)
    add_player(session_3)

    # add answers
    add_answer(session_1, state_bungejump, player_1, True)
    add_answer(session_1, state_murder, player_1, False)
    add_answer(session_1, state_bungejump, player_2, False)
    add_answer(session_2, state_publicsex, player_3, True)
    add_answer(session_3, state_bungejump, player_4, False)
    add_answer(session_3, state_publicsex, player_4, False)
    add_answer(session_3, state_murder, player_4, True)
    add_answer(session_3, state_stealing, player_4, False)
    add_answer(session_3, state_publicsex, player_5, False)
    add_answer(session_3, state_murder, player_5, True)
    add_answer(session_3, state_stealing, player_5, False)
    add_answer(session_3, state_redlight, player_5, True)

    # Print out what we have added to the user.
    for s in Statement.objects.all():
        print "Added '{}' (Categories: ".format(str(s)),
        for cat in s.categories.all():
            print "'" + str(cat) + "' ",
        print ")"


def add_category(name, adult_themed=False):
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
    p = Player.objects.get_or_create(session=session)[0]
    return p

def add_answer(session, statement, player, answer):
    a = Anwser.objects.get_or_create(session=session, statement=statement, player=player, answer=answer)[0]
    return a

# Start execution here!
if __name__ == '__main__':
    print "Starting NeverHaveIEver population script..."
    populate()