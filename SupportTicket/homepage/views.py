from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
                return redirect('/homepage')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        if request.user.is_authenticated:
            return redirect("/homepage")
        else:
            form = LoginForm()
    return render(request, 'homepage/login.html', {'form': form})

@login_required
def index(request):
    return render(request, 'homepage/index.html')

@login_required
def credit(request):
    return render(request, 'homepage/credit.html')


@login_required
def logoutUser(request):
    logout(request)
    return redirect('/login')