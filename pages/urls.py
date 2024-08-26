# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePageView, name='home'),  # Utiliza `views.homePageView` o cualquier vista que necesites
]