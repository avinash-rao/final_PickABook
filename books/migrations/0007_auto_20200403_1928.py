# Generated by Django 3.0.4 on 2020-04-03 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20200329_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(null=True, upload_to='book_images'),
        ),
    ]
