"""new_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from os import name
from django.contrib import admin
from django.urls import path
from blog.models import Blog
from destination_new.models import airport

from home.views import homeview
from contact.views import contactview
from blog.views import blogview
from destination_new.views import addview, airportview, destination_view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeview, name = "home"),
    path("home/",homeview, name="home"),
    path('contact/', contactview, name = 'contact'),
    path('blog/', blogview, name = 'blog'),
    path('destination/<int:id_val>/', destination_view, name='destination'),
    path("airport/", airportview, name="airport"),    
    path("addview/",addview , name="add-dest"),    


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)