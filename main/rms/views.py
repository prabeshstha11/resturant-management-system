from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, OrderedFood, Table
from .serializer import CategorySerializer, TableSerializer


## class based view
from rest_framework.views import APIView

class TableAPIView(APIView):
    def get(self, request):
        table = Table.objects.all()
        serializer = TableSerializer(table, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TableSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data) 
    
class TableDetailAPIView(APIView):
    def get(self, request, id):    
        table = Table.objects.get(id = id)
        serializer = TableSerializer(table)
        return Response(serializer.data)

    def post(self, request, id):
        serializer = TableSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data) 


## this is function based view

# Create your views here.
@api_view(["GET", "POST", "DELETE"])
def category(request):
    if request.method == "GET":
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(["GET", "POST", "DELETE"])
def category_detail(request, id):
    category = Category.objects.get(id=id)
    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        items = OrderedFood.objects.filter(food__category=category).count()
        
        if items > 0:
            return Response({"details":"Category cannot be deleted because it is listed in ordered food"})

        category.delete()
        return Response({"details":"Category deleted"})
