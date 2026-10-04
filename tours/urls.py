from django.urls import path

from . import views


urlpatterns = [
    # All available journeys.
    path(
        "",
        views.tour_list,
        name="tour_list",
    ),

    # Individual journey page.
    path(
        "<slug:slug>/",
        views.tour_detail,
        name="tour_detail",
    ),
]