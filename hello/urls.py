from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="Hello-Home"),
    path("about/", views.about, name="Hello-About"),
]