from django.urls import path
from . import views
urlpatterns = [
    path("home/", views.home),
    path("<int:id>/", views.post, name= "specific_post"),
    path("google/", views.visitGoogle),
    path("redirect/<int:id>/", views.redirectPost),
]