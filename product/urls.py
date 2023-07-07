from django.urls import path

from . import views

app_name = "product"
urlpatterns = [
    path("", views.home, name="home"),
    path("GetMeTheProduct/", views.product, name="GetMeTheProduct"),
    path("allusers/", views.all_users, name="allusers"),
]
