from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.views.generic import DetailView

from trainer.forms import TrainerForm, TrainerUpdateForm
from trainer.models import Trainer


class TrainerCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'trainer/create_trainer.html'
    model = Trainer
    form_class = TrainerForm
    success_url = reverse_lazy('list-trainers') # dupa salvarea datelor in tabela specificam unde sa fie redirectionat utilizatorul.
    success_message = 'Trainerul {fname} {lname} a fost adaugat cu succes. Adresa lui de email este: {email}.'

    def get_success_message(self, cleaned_data):
        return self.success_message.format(fname=self.object.first_name, lname=self.object.last_name, email=self.object.email)


class TrainerListView(LoginRequiredMixin, ListView):
    template_name = 'trainer/list_of_trainers.html'
    model = Trainer
    context_object_name = 'all_trainers'

    #
    def get_queryset(self):
        return Trainer.objects.filter(active=True)


class TrainerUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'trainer/update_trainer.html'
    model = Trainer
    form_class = TrainerUpdateForm
    success_url = reverse_lazy('list-trainers')


class TrainerDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'trainer/delete_trainer.html'
    model = Trainer
    success_url = reverse_lazy('list-trainers')


class TrainerDetailView(LoginRequiredMixin, DetailView):
    template_name = 'trainer/details_trainer.html'
    model = Trainer

@login_required
def delete_trainer_modal(request, pk):
    Trainer.objects.filter(id=pk).delete()

    return redirect('list-trainers')