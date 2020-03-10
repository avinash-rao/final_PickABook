from django.shortcuts import render

# Create your views here.


#HomePage
def firstpage(request):
    res = render(request,'LandingApp/firstpage.html')
    return res
