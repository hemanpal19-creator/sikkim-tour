from django.urls import path

from . import views


urlpatterns = [
    # The empty path represents the website homepage: "/".
    path("", views.home, name="home"),
]