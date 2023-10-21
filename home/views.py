from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


# TemplateView- este o clasa folosita pentru a afisa o pagina html (template)


class HomeTemplateView(TemplateView):
    template_name = 'home/homepage.html' # este folosita pentru a trece calea absoluta catre pagina .html

