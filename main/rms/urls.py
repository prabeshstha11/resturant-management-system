from django.urls import path
from .views import category, category_detail, TableAPIView, TableDetailAPIView

urlpatterns = [
    path("category", category), 
    path("category/<id>/", category_detail),
    
    path("table/", TableAPIView.as_view()),
    path("table/<id>/", TableDetailAPIView.as_view())

]
