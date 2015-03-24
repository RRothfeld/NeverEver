from django.shortcuts import render
from django import template

from neverever.models import Player, Statement
from neverever.forms import AnswerForm
from neverever.views import get_answer_forms


register = template.Library()

# template tag to be used in game play page
@register.inclusion_tag('neverever/answerButtons.html')
def get_answer_buttons(session):
	formlist = get_answer_forms(session)
	return {'formlist': formlist}
    
# template tag to be used in overall stats page
@register.inclusion_tag('neverever/statementTitles.html')
def get_statement_titles():
    statements = Statement.objects.all()

    return {'cat_name': "All", 'statements': statements}