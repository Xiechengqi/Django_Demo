from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import User
def index(request):
    return render(request,"index.html")
def login(request):
    return render(request,'login.html')
def regiest(request):
    return render(request,"regiest.html")
def user_index(request):
    if request.COOKIES.get("UserName"):
        getcookie = request.COOKIES.get("UserName")
        try:
            Objects = User.objects.get(UserName=getcookie)
            UserName = Objects.UserName
            UserPassword = Objects.UserPassword
            con = {
                "Head":UserName,
                "UserName":UserName,
                "PassWord":UserPassword
            }
            return render(request,"UserIndex.html",con)
        except:
            return HttpResponse(403)
    else:
        return render(request,"login.html")
def PageNotFound(request,exception):
    return render(request,"404.html")
def ServerForbidden(request,exception):
    return render(request,"403.html")
def ChangePassword(request):
    return render(request,"changepassword.html")