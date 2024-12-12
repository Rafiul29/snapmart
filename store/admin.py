from django.contrib import admin
from .models import Category, Product, Stock

# Register your models here.

class  CategoryAdmin(admin.ModelAdmin):
  list_display=['id','name']

class  ProductAdmin(admin.ModelAdmin):
  list_display=['id','name','category','price']
  

class  StockAdmin(admin.ModelAdmin):
  list_display=['id','product','quantity']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Stock,StockAdmin)
