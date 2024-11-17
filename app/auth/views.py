from django.contrib.auth.decorators import login_not_required
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse


@login_not_required
def login(request: HttpRequest):
    if request.user.is_authenticated:
        home_url = reverse('platform:home')
        return redirect(home_url)
    
    return render(request, 'auth/login.html')

@login_not_required
def register(request: HttpRequest):
    return render(request, 'auth/register.html')