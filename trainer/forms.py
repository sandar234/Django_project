from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Textarea, \
    DateInput, Select, CheckboxInput

from trainer.models import Trainer


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__' # in formularul generat in interfata se vor afisa toate fieldurile din modelul Student

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter your first name'}),
            'last_name':  TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter your last name'}),
            'course': TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter your course'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'departament': Select(attrs={'class': 'form-select'}),

        }


class TrainerUpdateForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control',
                                          'placeholder': 'Please enter your last name'}),
            'course': TextInput(attrs={'class': 'form-control',
                                       'placeholder': 'Please enter your course'}),
            'email': EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'Please enter your email'}),
            'departament': Select(attrs={'class': 'form-select'}),
        }
