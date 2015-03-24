from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test.client import Client

from neverever.models import Category, Statement, Session, Player
import populationScript


def add_category(name):
    c = Category.objects.get_or_create(name=name)[0]
    c = Category.objects.get_or_create(name=name)[0]
    return c


def add_statement(categories, title, views=0, nsfw=False):
    s = Statement.objects.get_or_create(title=title, views=views, nsfw=nsfw)[0]
    for category in categories:
        s.categories.add(category)
    s.save()
    return s


def add_session(sid, categories):
    s = Session.objects.get_or_create(sid=sid)[0]
    for category in categories:
        s.categories.add(category)
    s.save()
    return s


def add_player(stamp):
    p = Player.objects.get_or_create(stamp=stamp)[0]
    p.save()
    return


class IndexViewTests(TestCase):

    def test_index_view_status_code(self):
        """
        If it's not 200, there's obviously something wrong
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class IndexViewTests(TestCase):

    def test_play_view_status_code_no_categories_no_statements(self):
        """
        If it's not 200, there's obviously something wrong
        """
        response = self.client.get(reverse('play'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "We apologise but no categories have been found")

    def test_play_view_status_code_with_categories_no_statements(self):
        """
        If it's not 200, there's obviously something wrong
        """

        add_category("Testing")
        response = self.client.get(reverse('play'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "We apologise but no statements have been found")

    def test_play_view_status_code_with_categories_with_statements(self):
        """
        If it's not 200, there's obviously something wrong
        """

        cat = add_category("TestingCategory")
        cat2 = add_category("TestingCategory2")
        add_statement(categories=[cat],
                      title="TestingStatement",
                      nsfw=False)
        add_statement(categories=[cat, cat2],
                      title="TestingStatement2",
                      nsfw=True)

        #c = Client()
        response = self.client.get(reverse('play'))
        self.assertEqual(response.status_code, 302)  # Redirects to the same page


class AboutUsView(TestCase):
    def test_about_us_status_code(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class NewStatementView(TestCase):
    def test_new_statement_no_categories(self):
        response = self.client.get(reverse('play'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "We apologise but no categories have been found")

class Scripts(TestCase):
    def test_population_script(self):
        populationScript.populate()