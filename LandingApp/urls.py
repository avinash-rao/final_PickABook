from . import views
from django.conf.urls import url

urlpatterns=[
    url('^$',views.firstpage),
    url('login',views.userLogin),
    url('register',views.register),
    url('contact',views.contact),
    url('about',views.about),
    url('Reset-password',views.ChangePassword),
    url('Generate-password',views.GeneratePassword),
]
