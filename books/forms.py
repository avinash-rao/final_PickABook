from django.forms import ModelForm
from .models import *
from django import forms
from django.utils.translation import gettext_lazy as _

class BookForm(ModelForm):
    class Meta:
        model = Book
        # fields = '__all__'
        exclude = ['user_id', 'sold']
