from django.urls import path

from . import views

urlpatterns = [
    path("fibonacci/<int:num>", views.fibonacci),
]
