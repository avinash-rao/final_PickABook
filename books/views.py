from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from course.models import Course,CourseEntry
from django.contrib.auth.decorators import login_required

# Create your views here.
