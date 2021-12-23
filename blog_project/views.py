from django.http.response import HttpResponse
from django.urls import reverse
from django.shortcuts import render,HttpResponseRedirect

def home(request):
    return render(request,'home.html');
