from django.contrib import admin

from .models import *

# admin.site.register(Category)
# admin.site.register(Food)
# admin.site.register(Order)
admin.site.register(OrderedFood)
admin.site.register(Table)
admin.site.register(Payment)
admin.site.register(Reservation)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    search_fields = ['name']
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_price']
    search_fields= ['user', 'total_price']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Order, OrderAdmin)