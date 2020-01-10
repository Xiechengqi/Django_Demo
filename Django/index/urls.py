from django.urls import path
from . import views,user
from .views import *

handler403 = ServerForbidden
handler404 = PageNotFound

urlpatterns = [
    path("Index.html",views.index),
    path("",views.index),
    path("login.html",views.login,name="login.html"),
    path("regiest.html",views.regiest),
    path("login_api",user.login_api),
    path("RegiestApi",user.regiest_api),
    path("UserIndex.html",views.user_index,name="UserIndex.html"),
    path("changepassword.html",views.ChangePassword),
    path("ChangePasswordApi",user.ChangePassword)
]