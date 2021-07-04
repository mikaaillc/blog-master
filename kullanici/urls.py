from django.urls import path
from .views import *
app_name='kullanici'

urlpatterns = [

    path(r'login/',login_view,name='login'),
    path(r'register/',register_view,name='register'),
    path(r'logout/',logout_view,name='logout'),



]