from django.forms import ModelForm
from .models import *
from django import forms

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
