from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .models import Book, Genre
from .forms import BookForm

# Create your views here.
def bookss(request):
    res=render(request,'books/bookss.html')
    return res

def categoryBooks(request, category_name):
    # return HttpResponse("<h1>All the books of a particular category ("+ category_name +") will be displayed here.</h1>")
    genre = Genre.objects.filter(pk=category_name).exists()
    if (genre == False):
        return HttpResponse("<h1> No category with name "+ category_name +" </h1>")

    genre = Genre.objects.get(pk=category_name)
    books = genre.book_set.all()
    context = {'genre':genre, 'books':books}
    print("Displaying category page")
    return render(request, 'books/categorybooks.html', context)

def addBook(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BookForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            print('Form submitted')
            return HttpResponseRedirect('/books/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BookForm()

    return render(request, 'books/addbook.html', {'form': form})

def book_detail(request, book_id):
    #add if condition or exists function
    print(book_id, flush=True)

    #first checking if there is book of the mentioned id
    book = Book.objects.filter(pk=book_id).exists()
    if (book == False):
        return HttpResponse("<h1> No book with id "+ book_id +" </h1>")

    book = Book.objects.get(pk=book_id)
    context = {'book':book, }
    return render(request, 'books/book_detail.html', context)
