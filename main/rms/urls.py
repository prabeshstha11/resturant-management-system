from django.urls import path
from .views import category, category_detail

urlpatterns = [
    path("category", category),
    path("category/<id>/", category_detail)
    
]
