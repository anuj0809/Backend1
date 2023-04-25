from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.upload_music, name="upload_music"),
    
]
