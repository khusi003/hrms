"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.indexpage, name='home'),
    path('login/', views.login, name='login'),
    path('login-hr/',views.login_hr,name='login-hr'),
    path('profile/',views.profile,name='profile'),
    path('employees/',views.employees,name='employees'),
    path('add-employee/',views.add_employee,name='add-employee'),
    path('edit-employee/',views.edit_employee,name='edit-employee'),
    path('logout/',views.logout,name='logout'),
]
