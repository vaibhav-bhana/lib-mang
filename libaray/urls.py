
from django.urls import  path
from . import views

urlpatterns = [
    path('register',views.registers,name="register"),
    path('',views.login,name="login"),
    path("home",views.home.as_view(),name="home"),
    path("homee/<int:pk>",views.edit,name="homee"),
    path("home/<int:pk>",views.delete,name="delete"),
    path("index",views.index,name="index"),
    path("logout",views.Logout)
]