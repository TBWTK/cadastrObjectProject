from django import forms
from .models import Status, Estate, Person, LandPlot


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']


class EstateForm(forms.ModelForm):
    class Meta:
        model = Estate
        fields = ['name', 'status']


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name',
                  'surname',
                  'photo',
                  'estate']


class LandPlotForm(forms.ModelForm):
    class Meta:
        model = LandPlot
        fields = ['name',
                  'person',
                  'description']
