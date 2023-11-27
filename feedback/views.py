from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from feedback.forms import FeedbackForm
from feedback.models import Feedback


class FeedbackCreateView(LoginRequiredMixin, CreateView):
    template_name = 'feedback/create_feedback.html'
    model = Feedback
    form_class = FeedbackForm
    success_url = reverse_lazy('home_page')


class FeedbackListView(LoginRequiredMixin, ListView):
    template_name = 'feedback/list_of_feedbacks.html'
    model = Feedback
    context_object_name = 'all_feedbacks'
