from . import views
from django.conf.urls import url

urlpatterns=[
    url('^$',views.firstpage, name='index'),
    url('login',views.userLogin, name='login'),
    url('register',views.register, name='register'),
    url('about',views.about, name='about'),
]
