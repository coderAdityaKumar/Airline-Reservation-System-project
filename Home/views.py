from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="UserAccounts:LoginUser")
def index(request):
    # return HttpResponse("This is home. <br><a href=\"/accounts/logout\">Logout</a>")
    return render(request, 'Home/index.html')