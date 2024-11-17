from django.contrib.auth.decorators import login_not_required
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse


@login_not_required
def login(request: HttpRequest):
    print(request.user)
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        home_url = reverse('app:platform:home')
        return redirect(home_url)
    
    return render(request, 'auth/login.html')

@login_not_required
def register(request: HttpRequest):
    if request.user.is_authenticated:
        home_url = reverse('app:platform:home')
        return redirect(home_url)

    return render(request, 'auth/register.html')