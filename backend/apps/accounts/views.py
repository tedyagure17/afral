from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, "accounts/authentication/login.html")

def register_view(request):
    return render(request, "accounts/authentication/register.html")

def forgot_password_view(request):
    return render(request, "accounts/authentication/forgot-password.html")