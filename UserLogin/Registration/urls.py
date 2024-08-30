from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name= "Home"),
    path("register/",views.register,name="register"),
    path("logins/",views.logins,name="logins"),
    path("logout/",views.logout,name="logout")
]