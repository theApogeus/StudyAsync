# Generated by Django 5.0.1 on 2024-01-20 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0002_flashcard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flashcard',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='flashcard',
            name='user',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Flashcard',
        ),
    ]
