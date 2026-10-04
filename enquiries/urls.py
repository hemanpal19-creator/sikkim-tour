from django.urls import path

from . import views


urlpatterns = [
    path(
        "",
        views.enquiry_create,
        name="enquiry_create",
    ),
    path(
        "success/",
        views.enquiry_success,
        name="enquiry_success",
    ),
]