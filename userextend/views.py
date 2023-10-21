from datetime import datetime
from random import randint

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from djangoProject.settings import EMAIL_HOST_USER
from userextend.forms import UserForm
from userextend.models import History


# Create your views here.

class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')

    # def form_valid este o metoda pe care o puteti folosi pentru a suprascrie valoarile scrise in formal si nu numai
    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.title()
            # atribui valoarea new_user.first_name.title() campului first_name al obiectului new_user
            new_user.username = f'{new_user.first_name[0].lower()}{new_user.last_name.lower().replace(" ", "")}_{randint(100000, 999999)}'
            new_user.save()

            # send mail()
            subject = 'New account'
            message = f'Congratulatons! Your username is: {new_user.username}'
            send_mail(subject, message, EMAIL_HOST_USER, [new_user.email])

            # History
            history_text = f'{new_user.first_name} {new_user.last_name} was successfully created on {datetime.now()}'
            History.objects.create(text=history_text, created_at=datetime.now())



        return redirect('login')