from django.shortcuts import render
from django import template

from neverever.models import Player
from neverever.forms import AnswerForm


register = template.Library()

@register.inclusion_tag('neverever/answerButtons.html')
def get_answer_buttons(session):
    
    players = Player.objects.filter(session=session)

    forms = []

    for i in range(0, len(players)):  # +1 since a new player was added
        forms.append(AnswerForm(prefix="form" + str(i)))

    players = Player.objects.filter(session = session)
    formlist = zip(forms, players)
    
    return {'formlist': formlist}