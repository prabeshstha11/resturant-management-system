from django.urls import path
from .views import category, category_detail, TableAPIView, TableDetailAPIView, FoodGenericAPIView, FoodDetailGenericAPIView

urlpatterns = [
    path("category", category), 
    path("category/<id>/", category_detail),
    
    path("table/", TableAPIView.as_view()),
    path("table/<id>/", TableDetailAPIView.as_view()),
    
    path("food/", FoodGenericAPIView.as_view()),
    path("food/<id>/", FoodDetailGenericAPIView.as_view())

]
