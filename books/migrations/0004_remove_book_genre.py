# Generated by Django 3.0.4 on 2020-03-28 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
    ]
