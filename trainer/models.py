
from django.db import models

# Create your models here.
class Trainer(models.Model):

    departament_options = (
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('network', 'Network')
    )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    course = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    departament = models.CharField(choices=departament_options, max_length=8)
    active = models.BooleanField(default=True)
    profile = models.ImageField(upload_to='trainers_profile/', null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



# blank=True un camp nu este obligatoriu
# null= True  pt viitoarele modificari