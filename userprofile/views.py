from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
#deshboard page
@login_required(login_url="/login/")
def dashboard(request):
    if request.method=="GET":
      res=render(request,'userprofile/dashboard.html')
      return res

#profile editing page
@login_required(login_url="/login/")
def edit(request):
  if request.method=="POST":
      username=request.POST['username']
      print(username,"edit page")
      u = User.objects.get(username=username)
      res=render(request,'userprofile/edit.html',{'user':u})
      return res

#chnanging user data
@login_required(login_url="/login/")
def change(request):
    if request.method=="POST":
        print("under aa gye hai")
        username=request.POST['username']
        firstname=request.POST['firstname']
        mail=request.POST['mail']
        new_password=request.POST['password']
        if User.objects.filter(username=username).exists():
           u = User.objects.get(username=username)
           u.first_name=firstname
           u.email=mail
           u.set_password(new_password)
           u.save()
           messages.error(request, 'Profile updated Successfully')
           return HttpResponseRedirect("/",{})

@login_required(login_url="/login/")
def myprofile(request):
        # u=User.objects.get(id=request.GET['userid'])
        u = request.user
        return render(request,'userprofile/userprofile.html',{'user':u})

@login_required(login_url="/login/")
def logoutUser(request):
    data={}
    logout(request)
    return HttpResponseRedirect("/",{})
