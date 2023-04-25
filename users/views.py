from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect, render
from musics.models import Music
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm
from .models import User

# Create your views here.
def register(request):
    errors = None
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User()
            user.email = email
            user.set_password(password)
            user.save()
            return redirect(to='login')
        else:
            errors = list(form.errors.values())
            form.errors.clear()
            
    return render(request,'users/register.html',{'errors':errors})



def login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect(to='home')
        else:
            context['errors'] = ['Username or Password is incorrect']
    return render(request,'users/login.html',context)
