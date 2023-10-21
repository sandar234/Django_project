from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Textarea
from feedback.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class':'form-control',
                                           'placeholder': 'Please enter your last name'}),
            'email': EmailInput(attrs={'class': 'form-control','placeholder': 'Please enter your email'}),
            'message': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your message', 'rows': 4})
        }

