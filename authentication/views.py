from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('/')
        return render(request, '/auth/login', context={'massage': 'Invalid username or password'})
    return render(request, 'signin.html')


@login_required(login_url='/auth/login')
def logout_view(request):
    logout(request)
    return redirect('/auth/login')

