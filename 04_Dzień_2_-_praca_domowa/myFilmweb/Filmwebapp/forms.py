from .models import Person, Movie, PersonMovie
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from django import forms


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('first_name', 'last_name')
        labels = {'first_name': _('Imię'), 'last_name': _('Nazwisko')}


# class MovieForm(forms.Form):
#     title = forms.CharField(max_length=32)
#     genre = forms.CharField(max_length=32)
#     first_name_director =
#     last_name_director =
#     first_name_screenplay =
#     last_name_screenplay =
#     first_name_starring =
#     last_name_starring =
#     role =
#     year = forms.IntegerField(widget=forms.SelectDateWidget(years=range(1950, datetime.now().year)))
#     rating = forms.FloatField(max_value=10.0, min_value=1.0,
#                               widget=forms.NumberInput(attrs={'type': 'number', 'min': '1','max':'10','step':'0.01'}))


class PersonMovieForm(forms.ModelForm):

    class Meta:
        model = PersonMovie
        fields = ('role', )
        labels = {'role': _('jako')}
