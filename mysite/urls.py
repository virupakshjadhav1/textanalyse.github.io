"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views:
Function views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views 
from . import inside


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('analyse',views.analyse,name='analyse'),

    # by the use of the function like punctuation,about ,inside we can do it im backend
    
    #path('about',views.about,name='index'),
    #path('contact',views.contact,name='index'),
    #path('capitalize',views.capitalize,name='capitalize'),
    #path('uppercase',views.uppercase,name='uppercase'),
    #path('lowercase',views.lowercase,name='lowercase'),
    #path('inside',inside.i_am_inside,name='i_am_inside')
    #
]#
