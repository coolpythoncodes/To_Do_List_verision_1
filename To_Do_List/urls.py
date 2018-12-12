"""To_Do_List URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import To_do_app.views

urlpatterns = [
    path('',To_do_app.views.home,name="home"),
    path('about',To_do_app.views.about,name="about"),
    path('remove/<list_id>',To_do_app.views.remove,name="remove"),
    path('clear',To_do_app.views.clear,name="clear"),
    path('check/<list_id>',To_do_app.views.check,name="check"),
    path('uncheck/<list_id>',To_do_app.views.uncheck,name="uncheck"),
    path('admin/', admin.site.urls),
]
