# Generated by Django 4.2.5 on 2023-09-28 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_historystudent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historystudent',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
