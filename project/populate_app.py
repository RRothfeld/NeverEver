import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django

django.setup()

from neverhaveiever.models import Category, Statement


def populate():
    law_category = add_category('Law')

    add_statement(category=law_category,
                  title="Ran a red light"
    )

    add_statement(category=law_category,
                  title="Stole something",
    )

    add_statement(category=law_category,
                  title="Killed a man",
    )

    alcohol_category = add_category("Alcohol")

    add_statement(category=alcohol_category,
                  title="Threw up after drinking too much",
    )

    sex_category = add_category(name="Sex", adult_themed=True)

    add_statement(category=sex_category,
                  title="Had a threesome",
    )

    add_statement(category=sex_category,
                  title="Had sex in public",
    )

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for s in Statement.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(s))


def add_statement(category, title, views=0, answers=0):
    p = Statement.objects.get_or_create(category=category, title=title, views=views, answers=answers)[0]
    return p


def add_category(name, views=0, answers=0, adult_themed=False):
    c = Category.objects.get_or_create(name=name, views=views, answers=answers, adult_themed=adult_themed)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting NeverHaveIEver population script..."
    populate()