"""data_goog URL Configuration

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
from page_app import views as data_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', data_view.index1),
    path('add/', data_view.add_ab),
    path('add1/<int:a>/<int:b>/', data_view.add_ab_, name='add1'),
    path('index/', data_view.index, name='index'),
    path('index/upload/', data_view.upload, name='upload'),
    path('index1', data_view.index1, name='index1')
]
