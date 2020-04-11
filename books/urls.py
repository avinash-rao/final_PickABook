from . import views
from django.conf.urls import url
from django.urls import path

urlpatterns=[
    #localhost/books/
    path('',views.bookss, name='books'),

    #http://127.0.0.1:8000/books/category-hey
    url('(?:category-(?P<category_name>\w+))', views.categoryBooks),
    url('add-book', views.addBook, name='add-book'),

    #http://127.0.0.1:8000/books/book-detail/1
    url('book-detail/(?P<book_id>\d+)/order-book', views.order, name='order-book'),
    url('book-detail/(?P<book_id>\d+)', views.book_detail, name='book_detail'),
    url('search/', views.book_search, name='book_search'),
    
]
