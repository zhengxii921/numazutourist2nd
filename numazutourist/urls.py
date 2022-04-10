from django.urls import path
from . import views


app_name = "numazutourist"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("lovenumazu", views.LovenumaListView.as_view(), name="lovenumazu"),
    path("places", views.PlaceListView.as_view(), name="places"),
    path("add_place", views.PlaceCreateView.as_view(), name="add_place"),
    path("place_detail/<int:pk>/", views.PlaceDetailView.as_view(), name="place_detail"),
    path("place_update/<int:pk>/", views.PlaceUpdateView.as_view(), name="place_update"),
    path("add_lovenuma", views.LovenumaCreateView.as_view(), name="add_lovenuma"),
    path("lovenuma_detail/<int:pk>/", views.LovenumaDetailView.as_view(), name="lovenuma_detail"),
    path("lovenuma_update/<int:pk>/", views.LovenumaUpdateView.as_view(), name="lovenuma_update"),
    path("lovenuma_delete/<int:pk>/", views.LovenumaDeleteView.as_view(), name="lovenuma_delete"),
    path("user_detail/<int:pk>/", views.UserDetailView.as_view(), name="user_detail"),
    path("lovenuma_like/<int:pk>/", views.like, name="lovenuma_like"),
]

