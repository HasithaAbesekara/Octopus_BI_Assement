from django.urls import path
from . import views

urlpatterns = [
    path("", views.import_csv_view, name="import_csv"),
    path("display-data/", views.display_data_view, name="display_data"),
]
