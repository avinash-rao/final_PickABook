from . import views
from django.conf.urls import url

urlpatterns=[
    #localhost/books/
    url('^$',views.bookss, name='books'),
    url('(?:category-(?P<category_name>\w+))', views.categoryBooks),
    url('add-book', views.addBook),

    #http://127.0.0.1:8000/books/book-detail/1
    url('book-detail/(?P<book_id>\d+)', views.book_detail),

]
