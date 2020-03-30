from . import views
from django.conf.urls import url

urlpatterns=[
    url('^$',views.firstpage, name='index'),
    url('login',views.userLogin, name='login'),
    url('register',views.register, name='register'),
    # url('contact',views.contact, name='contact'),
    url('about',views.about, name='about'),
    url('Reset-password',views.ChangePassword, name='changePassword'),
    url('Generate-password',views.GeneratePassword, name='generatePassword'),
]
