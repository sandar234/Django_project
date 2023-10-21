import django_filters
from django import forms

from student.models import Student
from trainer.models import Trainer


# iN ACEST FISIER STABILITI FIELDURILE PE CARE LE DORITI IN FORMULAR DE FILTRARE

#lookup_exp -> icontains, exact, startswith, endswith, lte, gte, lt gt

# gte -> greater than or equal to
# gt -> greater than

# lte -> less than or equal to
# lt  -> less to

class StudentFilter(django_filters.FilterSet):

    first_name = django_filters.CharFilter(lookup_expr='icontains', label='First name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = django_filters.CharFilter(lookup_expr='startswith', label='Last name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = django_filters.NumberFilter( widget=forms.NumberInput(attrs={'class': 'form-control'}))

    list_of_trainers = [(trainer.id, f'{trainer.first_name} {trainer.last_name}') for trainer in Trainer.objects.filter(active=True)]
    print(list_of_trainers)
    trainer = django_filters.ChoiceFilter(choices=list_of_trainers, widget=forms.Select(attrs={'class': 'form-select'}))

    start_date_gte = django_filters.DateFilter(field_name='start_date', lookup_expr='gte', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    start_date_lte = django_filters.DateFilter(field_name='start_date', lookup_expr='lte', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age',
                  'start_date_gte', 'start_date_lte', 'trainer']