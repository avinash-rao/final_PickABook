from . import views
from django.conf.urls import url

urlpatterns=[
    url('^$',views.firstpage),
]
