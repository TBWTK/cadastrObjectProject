"""realEstate URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from estateApp import views


urlpatterns = [
    path('', views.index),
    path('createLandPlot/', views.createLandPlot),
    path('displayStatus/', views.displayStatus),
    path('displayStatus/createStatus/', views.createStatus),
    path('displayEstate/', views.displayEstate),
    path('displayEstate/createEstate/', views.createEstate),
    path('displayPerson/', views.displayPerson),
    path('displayPerson/createPerson/', views.createPerson),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
# мб в нем трабл, там так же в консоли он настраиватеся, через те команды