# Generated by Django 3.0.3 on 2023-05-09 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='budget',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='fees_in_usa',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='fess_in_world',
        ),
    ]