from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse
from django.contrib import messages
from django.db.models import Count, Q
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .models import Book, Genre, Order
from .forms import BookForm

# Create your views here.
def bookss(request):
    books = Book.objects.filter(sold=False).order_by('-date')
    context = {'books': books}
    return render(request,'books/bookss.html', context)

def categoryBooks(request, category_name):
    genre = Genre.objects.filter(pk=category_name).exists()
    if (genre == False):
        print("not found")
        return HttpResponse("<h1> No category with name "+ category_name +" </h1>")
    genre = Genre.objects.get(pk=category_name)
    books = genre.book_set.filter(sold=False)
    context = {'genre':genre, 'books':books}
    print("Displaying category page")
    return render(request, 'books/categorybooks.html', context)

@login_required(login_url="/login/")
def addBook(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BookForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # to add value to user field
            book = form.save(commit=False)
            book.user_id = request.user
            book.save()
            # form.save()
            print('New book Form submitted')
            return HttpResponseRedirect(reverse('books'))
        else:
            print("Invalid form")
            print(form.errors)
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

@login_required(login_url="/login/")
def order(request, book_id):
    book = Book.objects.filter(pk=book_id).exists()
    if (book == False):
        return HttpResponse("<h1> No book with id "+ book_id +" </h1>")
    book = Book.objects.get(pk=book_id)
    u = request.user
    total = book.actual_price
    Order.objects.create(user_id=u, book_id=book, total=total)
    book.sold = True
    book.save()
    send_mail(
    'PickABook | Order placed successfully',
    'We would love to inform you that your order has been successfully placed and would be reaching you soon. Ordered book:'+book.title,
    'rahulgeorge0009@gmail.com',
    [u.email,],
    fail_silently=False,
    )
    messages.error(request, 'Your order has been placed')
    return HttpResponseRedirect(reverse('index'))

def book_search(request):
     if request.method == 'GET':
        query= request.GET.get('q')
        if query is not None:
            title_lookups= Q(title__icontains=query)
            author_lookups = Q(author__icontains=query)

            title_results = Book.objects.filter(title_lookups).distinct()
            author_results = Book.objects.filter(author_lookups).distinct()
            context = {'title_results': title_results, 'author_results': author_results}
            return render(request, 'books/search.html', context)
        else:
            return render(request, 'books/search.html')
     else:
        return render(request, 'books/search.html')
