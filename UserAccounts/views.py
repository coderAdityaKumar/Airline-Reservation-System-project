from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginUser(request):
    if request.method == 'POST':
        uname = request.POST['username']
        paswd = request.POST['password']

        user = authenticate(username=uname, password=paswd)
        if user is not None:
            login(request, user)
            # return redirect('home')
            return redirect("Home:IndexHome")
        else:
            return HttpResponse("Wrong username and password.")
    return render(request, 'UserAccounts/login.html')

def signUpUser(request):
    if request.method == 'POST':
        fname = request.POST['firstName']
        lname = request.POST['lastName']
        uname = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm-password']

        if User.objects.filter(email=email).exists():
            return HttpResponse('Account with this email already exists.<br>Try login ...')
        else:
            my_user = User.objects.create_user(username=uname, email=email, password=pass1)
            my_user.first_name = fname
            my_user.last_name = lname
            my_user.save()
            return redirect('UserAccounts:LoginUser')
    return render(request, 'UserAccounts/signup.html')

def logoutUser(request):
    logout(request)
    return redirect('UserAccounts:LoginUser')