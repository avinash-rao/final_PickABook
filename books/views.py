from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .forms import BookForm

# Create your views here.
def bookss(request):
    res=render(request,'books/bookss.html')
    return res

def addBook(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BookForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print('Form submitted')
            return HttpResponseRedirect('/books/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BookForm()

    return render(request, 'books/addbook.html', {'form': form})
