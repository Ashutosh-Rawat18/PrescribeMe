from django.urls import path
from . import views

urlpatterns = [
    path("log", views.log, name="log"),
    path("logout", views.logout, name="logout")
]
