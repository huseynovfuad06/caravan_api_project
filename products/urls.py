from django.urls import path
from . import views

app_name = "products"


urlpatterns = [
    path("list/", views.ProductListView.as_view(), name="list")
]