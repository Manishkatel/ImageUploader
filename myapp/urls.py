from django.urls import path
from . import views  # Import views from the app

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('delete/<int:pk>/', views.delete_image, name='delete_image'),  # Delete image
    path('edit/<int:pk>/', views.edit_image, name='edit_image'),  # Edit image
]
