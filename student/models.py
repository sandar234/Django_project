from django.contrib.auth.models import User
from django.db import models

from trainer.models import Trainer


# Create your models here.

class Student(models.Model):

    gender_options = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    first_name = models.CharField(max_length=31)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=50)
    description = models.TextField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)
    gender = models.CharField(choices=gender_options, max_length=6)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)
    profile = models.ImageField(upload_to='profiles/', null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #auto_now_add=True stocheaza data si ora cand a fost adaugata inregistrarea in tabela. Nu se mai modifica data si ora
    #auto_now = True stocheaza data si ora cand se realizeaza modificari pe respectiva inregistrare.

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


    #cele 2 comenzi IMPORTANTE pt a se salva fiecare modificare
    #python manage.py makemigrations
    #python manage.py migrate


class HistoryStudent(models.Model):
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.message
