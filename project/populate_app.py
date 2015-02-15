import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django

django.setup()

from neverhaveiever.models import Category, Statement


def populate():
    law_category = add_category('Law')

    add_statement(categories=[law_category],
                  title="Ran a red light",
                  views=130,
                  yes_answers=40,
                  no_answers=50,
                  )

    add_statement(categories=[law_category],
                  title="Stole something",
                  views=70,
                  yes_answers=15
    )

    add_statement(categories=[law_category],
                  title="Killed a man",
                  no_answers=50
    )

    alcohol_category = add_category("Alcohol")

    add_statement(categories=[alcohol_category],
                  title="Threw up after drinking too much",
                  views=600
    )

    add_statement(categories=[alcohol_category, law_category],
                  title="Got drunk when I was 15",
                  views=600
    )

    sex_category = add_category(name="Sex", adult_themed=True)

    add_statement(categories=[sex_category],
                  title="Had a threesome",
                  views=500
    )

    add_statement(categories=[sex_category],
                  title="Had sex in public",
                  views=500
    )

    # Print out what we have added to the user.
    for s in Statement.objects.all():
        print "Added '{}' (Categories: ".format(str(s)),
        for cat in s.categories.all():
            print "'" + str(cat) + "' ",
        print ")"


def add_statement(categories, title, views=0, yes_answers=0, no_answers=0):
    s = Statement.objects.get_or_create(title=title, views=views,
                                        yes_answers=yes_answers, no_answers=no_answers)[0]
    for category in categories:
        s.categories.add(category)
    s.save()
    return s


def add_category(name, adult_themed=False):
    c = Category.objects.get_or_create(name=name, adult_themed=adult_themed)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting NeverHaveIEver population script..."
    populate()