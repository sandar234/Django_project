from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
@login_required
def index(request):
    return HttpResponse('Hello World!')

@login_required
def name(request):
    return HttpResponse('Hello, Sanda')

@login_required
def cars(request):
    context = {
        'all_cars': [
            {
                'brand': 'Audi',
                'model': 'RS',
                'year': 2023
            },
            {
                'brand': 'Mercedes',
                'model': 'E63',
                'year': 2022
            },
            {
                'brand': 'Porsche',
                'model': 'Panamera',
                'year': 2024
            }
        ]
    }
    return render(request, 'intro/list_of_cars.html', context)

@login_required
def movies(request):
    netflix = {
        'all_movies': [
            {
                'name': 'My fault',
                'gen': 'Romantic',
                'year': 2023
            },
            {
                'name': 'The Interpreter',
                'gen': 'Action',
                'year': 2022

            },
            {
                'name': 'Miracle',
                'gen': 'Psihologic',
                'year': 2021
            }
        ]
    }
    return render(request, 'intro/list_of_movies.html', netflix)
