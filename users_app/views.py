from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here

def signin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    return render(request,'signin.html')

@login_required
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('users_app:signin'))

