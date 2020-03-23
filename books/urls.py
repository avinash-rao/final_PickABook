from . import views
from django.conf.urls import url

urlpatterns=[
    url('^$',views.bookss),
    url('add-book', views.addBook),
]
