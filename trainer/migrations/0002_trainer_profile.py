# Generated by Django 4.2.5 on 2023-09-20 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='profile',
            field=models.ImageField(null=True, upload_to='profiles/'),
        ),
    ]
