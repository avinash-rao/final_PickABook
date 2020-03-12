from userprofile import views
from django.conf.urls import url
urlpatterns=[

url('^$',views.dashboard),
url('edit',views.edit),
url('change',views.change),
url('myprofile',views.myprofile),
url('logout',views.logoutUser),
]
