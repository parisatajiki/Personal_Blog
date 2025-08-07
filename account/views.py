from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserEditForm


def login_page(request):
    if request.user.is_authenticated == True:
        return redirect('home_app:home')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:  # یوزر شناختته شده بود
            login(request, user)
            return redirect('home_app:home')
    return render(request, 'account/login.html', {})


def user_register(request):
    context = {"errors": []}
    if request.user.is_authenticated == True:
        return redirect('home_app:home')
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            context['errors'].append("Passwords are not same")
            return render(request, "account/register.html", context)

        user = User.objects.create_user(username=username, email=email, password=password1)
        # user = User.objects.create(username=username,password=password1,email=email)
        login(request, user)
        return redirect('home_app:home')
    return render(request, "account/register.html", {})


def user_logout(request):
    logout(request)
    return redirect('home_app:home')


def edit_profile(request):
    if request.method == "POST":
        form = UserEditForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'account/edit.html', {"form": form})
