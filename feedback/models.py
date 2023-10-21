from django.db import models

# Create your models here.


class Feedback(models.Model):

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)

    message = models.TextField(max_length=400)
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


    # Null = True pt a adauga eventualele modificari ulterioare