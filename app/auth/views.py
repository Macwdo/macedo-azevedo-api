from django.shortcuts import render


def login(request):
    context = {
        "title": "Login",
    }
    return render(request=request, template_name="login.html", context=context)