from userprofile import views
from django.conf.urls import url
urlpatterns=[
url('^$',views.myprofile, name='myprofile'),
url('edit',views.edit, name="edit"),
url('logout',views.logoutUser),
url('myorders', views.myorders, name='myorders')
]
