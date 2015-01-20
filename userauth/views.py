from django.shortcuts import redirect, render
from forms import UserProfileForm, UserForm
from django.http import HttpResponse, HttpResponseRedirect
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
            return redirect('accounts/login/')
    else:
        form = UserForm()
    c = {'form' : form}
    return render(request,'register.html',c)

def user_login(request):
    next = ""

    if request.GET:  
        next = request.GET['next']
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if next == "":
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect(next)
        else:
            return HttpResponse('Invalid user name or password')
    else:
        x = {'next': next}
        return render(request, 'login.html', x) 

def logout_view(request):
    logout(request)
    return redirect('/')
