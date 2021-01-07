from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from main.forms import CustomUserCreationForm

def main(request):
    return render(request, "main/main.html")

def dashboard(request):
    return render(request, "main/dashboard.html")

def profile(request):
    return render(request, "main/profile.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "registration/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
