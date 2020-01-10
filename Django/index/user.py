from django.shortcuts import render
from .models import User
from django.shortcuts import reverse,redirect,HttpResponse


def regiest_api(request):
    user_name=""
    user_password = ""
    if request.method == "GET":
        return redirect(reverse("regiest"))
    else:
        user_name = request.POST["UserName"]
        user_password = request.POST["password"]
        if user_password and user_name:
            try:
                if User.objects.get(UserName=user_name):
                    con = {
                        "error_idset":"error_messge_check",
                        "error_messge":"已经拥有这个用户"
                    }
                    print(1)
                    return render(request,"regiest.html",con)
            except:
                save_data = User.objects.create(UserName=user_name,UserPassword=user_password)
                save_data.save()
                print("ok")
                return redirect(reverse("login.html"))
        else:
            con = {
                "error_idset": "error_messge_check",
                "error_messge": "你没有输入密码!或用户名!"
            }
            print(2)
            return render(request, "regiest.html", con)

def login_api(request):
    user_password = ""
    user_name = ""
    user_check = ""
    if request.method == "GET":
        return redirect("login.html")
    else:
        user_password = request.POST["password"]
        user_name = request.POST["UserName"]
        if user_name and user_password:
                user_check = User.objects.get(UserName=user_name)
                if user_check.UserPassword == user_password:
                    con = {
                        "rlt":"登录成功!"
                    }
                    print("ok")
                    userid=user_check.id
                    response = redirect(reverse("UserIndex.html"))
                    response.set_cookie("UserName",user_name,max_age=60*60*24)
                    response.set_cookie("id",userid,max_age=60*60*24)
                    return response
                else:
                    con = {
                        "error_idset":"error_messge_check",
                        "error_messge":"密码错误!"
                    }
                    print("1")
                    return render(request,"login.html",con)
                con = {
                    "error_idset": "error_messge_check",
                    "error_messge": "没有这个用户哦:D!"
                }
                print("2")
                return render(request,"login.html",con)
        else:
            con = {
                "error_idset": "error_messge_check",
                "error_messge": "你没有输入用户/密码"
            }
            print("3")
            return render(request, "login.html",con)
def ChangePassword(request):
    oldpassword = ""
    newpassword = ""
    UserName = ""
    if request.method =="GET":
        return render(request,"changepassword.html")
    else:
        oldpassword = request.POST["oldpassword"]
        newpassword = request.POST["newpassword"]
        UserName = request.POST["UserName"]
        UserObjects = User.objects.get(UserName=UserName)
        if UserObjects.UserPassword == oldpassword:
            UserObjects.UserPassword=newpassword
            UserObjects.save()
            userid = UserObjects.id
            response = redirect(reverse("UserIndex.html"))
            response.set_cookie("UserName", UserName, max_age=60 * 60 * 24)
            response.set_cookie("id", userid, max_age=60 * 60 * 24)
            return response
        return HttpResponse("密码/用户名错误")





