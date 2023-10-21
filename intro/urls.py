from django.urls import path

from intro import views

urlpatterns = [
    path('first_page/', views.index, name='first-page'),
    path('show_name/', views.name, name='show-name'),
    path('list_cars/', views.cars, name='list-cars'),
    path('list_movies/', views.movies, name='list-movies')
]

# pentru fiecare clasa/def definita in views.py vom
# defini un path nou in lista numita urlpatterns


# PREFIXUL din path() TREBUIE sa fie UNIC
# NAME-UL din path() TREBUIE SA FIE UNIC