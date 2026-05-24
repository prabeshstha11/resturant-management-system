from django.contrib import admin

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    # list_filter = ['name']

class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    search_fields = ['name']
    list_filter = ['price', 'category']
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_price']
    search_fields= ['user', 'total_price']
    list_filter = ['status', 'user']
    
class TableAdmin(admin.ModelAdmin):
    list_display = ['number', 'capacity', 'is_available']
    search_fields = ['capacity']
    list_filter = ['capacity']
    
class OrderedFoodAdmin(admin.ModelAdmin):
    list_display = ['order', 'food']
    list_filter = ['order', 'food']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(OrderedFood, OrderedFoodAdmin)

admin.site.register(Payment)
admin.site.register(Reservation)