from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserLoginForm


def sign_up(request):
    context = {}
    context['form'] = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email', None)
            username = form.cleaned_data.get('username', None)
            password = form.cleaned_data.get('password1', None)

            auth_user = authenticate(email=email, password=password, username=username)

            try:
                login(request, auth_user)
            except Exception, e:
                print e
                return HttpResponse('invalid user, try again <a href="/signup/">here</a>')
    return render(request, 'signup.html', context)


def login_view(request):
    context = {}
    context['form'] = CustomUserLoginForm()
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        context['form'] = form

        if form.is_valid():
            email = form.cleaned_data.get('email', None)
            password = form.cleaned_data.get('password', None)

            auth_user = authenticate(username=email, password=password)

            try:
                login(request, auth_user)

            except Exception, e:
                message = """
				User or password is incorrect, try again
				<a href="/signin/">Login</a>
				"""
                return HttpResponse(message)
    return render(request, 'signin.html', context)


def logout_view(request):
    logout(request)

    return redirect('/signup/')
