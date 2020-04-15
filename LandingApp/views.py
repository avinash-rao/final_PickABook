from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from books.models import Book,Genre,Language
from django.db.models import Count, Q
# Create your views here.

#HomePage
def firstpage(request):
    categories = Genre.objects.annotate(book_count=Count('book', filter=Q(book__sold=False))).order_by('-book_count')
    context = {'categories': categories}
    res = render(request,'LandingApp/firstpage.html', context)
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
       first_name=request.POST['fnamesignup']
       last_name = request.POST['lnamesignup']
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
          last_name=last_name,
          )
          #user.save()
          print("shi hai")
          messages.error(request, 'Successeful signup go for Login')
          return HttpResponseRedirect("/",data)
    else:
        return HttpResponse("<h1> out </h1>");


#contact page
# @login_required(login_url="/login/")
# def contact(request):
#     res=render(request,'LandingApp/contact.html')
#     return res

#about page
def about(request):
    res=render(request,'LandingApp/about.html')
    return res

#
# def resetPassword(request):
#     data={};
#     if request.method=="POST":
#         mail=request.POST['mail']
#         if User.objects.filter(username=mail).exists():
#             print("user exists");
#             usr = User.objects.get(username=mail)
#             print(usr.email)
#             send_mail(
#                      'PickABook',
#                      '''We heard that you lost your PickABook password. Sorry about that!
#                     But dont worry! You can use the following link to reset your password
#                     http://localhost:8000/Generate-password?username='''+usr.username,
#
#                      'rao.avinash@gmail.com',
#                      ['rao.avinash@gmail.com'],
#                      fail_silently=False,
#                      )
#             messages.error(request, "Email has been sent check your email.")
#             return HttpResponseRedirect('/',data)
#         else:
#             messages.error(request, "Email does not exists")
#             return HttpResponseRedirect('/',data)
#     else:
#         return render(request,'LandingApp/Resetpassword.html');
#         # return render(request,'Landingapp/firstpage.html');
#
#
# def GeneratePassword(request):
#     data={};
#     if request.method=="POST":
#         username=request.POST['username']
#         createpassword=request.POST['createpassword']
#         confirmpassword=request.POST['confirmpassword']
#         print(createpassword,username,confirmpassword)
#         user=User.objects.get(username=username)
#         user.set_password(createpassword)
#         user.save()
#         messages.error(request, "Password has been changed.")
#         return HttpResponseRedirect('/',data)
#     else:
#         return render(request,'LandingApp/generatePass.html');
