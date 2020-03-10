from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.


#HomePage
def firstpage(request):
    res = render(request,'LandingApp/firstpage.html')
    return res

#login user
def userLogin(request):
    data={}
    user=0
    if request.method=="POST":
        mail=request.POST['mail']
        password=request.POST['password']
        print(mail,password)
        user=authenticate(request,username=mail,password=password)
        if user:
            login(request,user)
            request.session['username']=mail
            return HttpResponseRedirect('profile',user)
        else:
            messages.error(request, 'Invalid Credentials!!')
            return HttpResponseRedirect("/",data)
    else:
        data={}
        res=render(request,'Landingapp/firstpage.html')
        return res

#user Registration
def register(request):
    data={}
    if request.method=="POST":
       first_name=request.POST['namesignup']
       username=request.POST['emailsignup']
       password=request.POST['passwordsignup']
       passwords_confirm=request.POST['passwordsignup_confirm']
       mail=request.POST['emailsignup']
       # if User.objects.filter(username=mail).exists():
       #     messages.error(request, 'Membership teken already')
       #     return HttpResponseRedirect("/",data)
       #     print("username is taken")
       if User.objects.filter(email=mail).exists():
           messages.error(request, 'Email already exists!!')
           return HttpResponseRedirect("/",data)
           print("email exists already")

       elif  password != passwords_confirm:
            messages.error(request, 'Password not matched!!')
            return HttpResponseRedirect("/",data)
       else:
          user = User.objects.create_user(
          username=mail,
          password=password,
          email=mail,
          first_name=first_name,
          )
          #user.save()
          print("shi hai")
          messages.error(request, 'Successeful signup go for Login')
          return HttpResponseRedirect("/",data)
    else:
        return HttpResponse("<h1> out </h1>");
