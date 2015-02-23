from django import forms
from neverever.models import Statement, Category


class StatementForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Never have I ever ")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    no_answers = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    yes_answers = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    category_list = []
    for cat in Category.objects.all():
        category_list.append((cat.id, cat))

    categories = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                           choices=category_list)

    class Meta:
        model = Statement
        fields = ('title', 'categories')