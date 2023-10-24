"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from maidapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name = "home"),
    path("request_maid", views.request_maid, name="request_maid"),
    path("request_cook", views.request_cook, name="request_cook"),
    path("request_nanny", views.request_nanny, name="request_nanny"),
    path('add_service_provider/', views.add_service_provider, name='add_service_provider'),
    path('add_service_provider/add_maid/', views.add_maid, name='add_maid'),
    path('add_service_provider/add_cook/', views.add_cook, name='add_cook'),
    path('add_service_provider/add_nanny/', views.add_nanny, name='add_nanny'),
    path("add_customer", views.add_customer, name='add_customer'),
    path("success-page", views.success_page, name='success_page'),
    path("book_provider", views.book_provider, name='book_provider'),
    path('make_service_provider_available/<str:selected_service>/<int:provider_id>/', views.make_service_provider_available, name='make_service_provider_available'),
]
