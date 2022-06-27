from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'Acest username deja exista')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Acest email e deja folosit')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Parola nu este la fel')
            return redirect('register')

    else:
        return render(request, 'register.html')

def login(request):

    if request.method == 'POST':

        username2 = request.POST['username']
        password2 = request.POST['password']

        user = auth.authenticate(username=username2, password=password2)
        
        if user is not None:

            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'Username or password is wrong')
            return redirect('login')
    else:

        return render(request, 'login.html') 

def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request, pk):
    return render(request, 'post.html', {'pk': pk})

