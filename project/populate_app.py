import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django

django.setup()

from neverever.models import Category, Statement


def populate():
    # add categories
    cat_nsfw = add_category("NSFW")
    cat_violence = add_category("Violence")
    cat_illegal = add_category("Illegal")
    cat_alcohol = add_category("Alcohol")
    cat_sexual = add_category("Sexual")
    cat_activity = add_category("Activities")

    # add statements
    add_statement(categories=[cat_activity],
                  title="been bungee jumping",
                  views=10,
                  )

    add_statement(categories=[cat_illegal],
                  title="run a red light",
                  views=130,
                  )

    add_statement(categories=[cat_nsfw, cat_illegal],
                  title="stolen something",
                  views=70
    )

    add_statement(categories=[cat_nsfw, cat_violence],
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

    add_statement(categories=[cat_nsfw, cat_sexual],
                  title="Had sex in public"
    )

    # add sessions
    add

    # add players
    # add answers

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

# add further categories! TODO raoul

# Start execution here!
if __name__ == '__main__':
    print "Starting NeverHaveIEver population script..."
    populate()