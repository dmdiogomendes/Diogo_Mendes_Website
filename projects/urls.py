from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Route for home page
    path('post/<int:post_id>/', views.post_detail, name='post'),
]