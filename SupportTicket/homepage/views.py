from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .script.forms import LoginForm
from django.contrib import messages

def loginUser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {user.username}!')
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'homepage/login.html', {'form': form})

def index(request):
    return render(request, 'homepage/index.html')