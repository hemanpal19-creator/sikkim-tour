from django.urls import path

from . import views


urlpatterns = [
    # All available stays.
    path(
        "",
        views.stay_list,
        name="stay_list",
    ),

    # Individual stay page.
    path(
        "<slug:slug>/",
        views.stay_detail,
        name="stay_detail",
    ),
]