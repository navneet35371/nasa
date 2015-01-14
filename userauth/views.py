from django.shortcuts import *
from forms import UserProfileForm, UserForm
from django.http import HttpResponse
from userauth.models import UserProfile
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            print request.POST
            my_model = form.save(commit=False)
            my_model.set_password(request.POST['password'])
            my_model.save()
            return redirect('/login')
    else:
        form = UserForm()
    c = {'form' : form}
    return render(request,'register.html',c)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('Invalid user name or password')
    else:
        return render(request, 'login.html') 

def logout_view(request):
    logout(request)
    return redirect('/login/')
