from django.urls import path
from . import views

urlpatterns = [
    path("post/<int:pk>/", views.post, name="post")
]
