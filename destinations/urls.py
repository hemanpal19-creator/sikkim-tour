from django.urls import path

from . import views


urlpatterns = [
    # One URL pattern handles every destination using its slug.
    path(
        "<slug:slug>/",
        views.destination_detail,
        name="destination_detail",
    ),
]