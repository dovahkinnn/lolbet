from django.urls import path
from . import views



urlpatterns = [
    path("",views.index),
    path("a",views.login),
    path("anasayfa/",views.anasayfa),
    path("signin/",views.signin),


    
]
