from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Textarea, \
    DateInput, Select

from student.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__' # in formularul generat in interfata se vor afisa toate fieldurile din modelul Student

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter your first name'}),
            'last_name':  TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter your last name'}),
            'age': NumberInput(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter your age'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your description', 'rows': 3}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}), #type="datetime-local"
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}), #type="datetime-local"
            'gender': Select(attrs={'class': 'form-select'}),
            'trainer': Select(attrs={'class': 'form-select'}),
        }

    def clean(self):
        cleaned_data = self.cleaned_data  # stocam un dictionar cu toate valorile completate de utilizator in formular


        # unicitate pe adresa de email
        get_email = cleaned_data['email']  # stocam valoarea introdusa de utilizator in input email din formular
        check_emails = Student.objects.filter(email=get_email)   # cautam in tabela student_student daca exista in coloana email valoarea din get_email
        if check_emails: # daca exsita o adresa de email deja salvata in tabela
            msg = 'Exista deja aceasta adresa de email'
            self._errors['email'] = self.error_class([msg])  # afisam eroarea in formualar pentru campul email

        # daca start_date este mai mare decat end_date
        get_start_date = cleaned_data['start_date']
        get_end_date = cleaned_data['end_date']

        if get_start_date > get_end_date:
            msg = 'Nu poate fi start date mai mare decat end date'
            self._errors['start_date'] = self.error_class([msg])

        # campul description sa contina minim 10 caractere

        get_description = cleaned_data['description']
        if len(get_description) < 10:
            msg = 'Trebuie sa adaugi minim 10 caractere'
            self._errors['description'] = self.error_class([msg])


        # first_name si last_name sa fie unic
        get_first_name = cleaned_data['first_name']
        get_last_name = cleaned_data['last_name']

        check_fname_lname = Student.objects.filter(first_name=get_first_name, last_name=get_last_name)
        if check_fname_lname:
            msg = 'Exista deja un student cu acest nume'
            self._errors['first_name'] = self.error_class([msg])
            #self._errors['last_name'] = self.error_class([msg])


        return cleaned_data

# Class Meta folosit pentru a furniza metadale si configurat in plus formularului



class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__' # in formularul generat in interfata se vor afisa toate fieldurile din modelul Student

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter your first name'}),
            'last_name':  TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter your last name'}),
            'age': NumberInput(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter your age'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your description', 'rows': 3}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}), #type="datetime-local"
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}), #type="datetime-local"
            'gender': Select(attrs={'class': 'form-select'}),
            'trainer': Select(attrs={'class': 'form-select'}),
        }


