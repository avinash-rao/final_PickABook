from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import forms
from books.models import Order

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
    user = request.user
    form = forms.UpdateProfile(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('myprofile')
    return render(request, 'userprofile/edit.html', {'form': form})

@login_required(login_url="/login/")
def myprofile(request):
        # u=User.objects.get(id=request.GET['userid'])
        u = request.user
        return render(request,'userprofile/userprofile.html',{'user':u})

def myorders(request):
    user = request.user
    orders = Order.objects.filter(user_id=user.id).select_related('book_id').order_by('date')
    print(orders)
    context = {'orders':orders}
    return render(request, 'userprofile/myorders.html', context)

@login_required(login_url="/login/")
def logoutUser(request):
    data={}
    logout(request)
    return HttpResponseRedirect("/",{})
