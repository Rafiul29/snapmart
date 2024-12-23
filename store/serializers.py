from rest_framework import serializers
from .models import Category, Product, Stock

class CategorySerializer(serializers.ModelSerializer):

  class Meta:
    model=Category
    fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
  category=CategorySerializer()

  class Meta:
    model=Product
    fields='__all__'


class StockSerializer(serializers.ModelSerializer):
  product=ProductSerializer()

  class Meta:
    model =Stock
    fields='__all__'