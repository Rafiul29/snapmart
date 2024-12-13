from django.shortcuts import render
from rest_framework import viewsets
from .models import Category,Product,Stock
from .serializers import CategorySerializer,ProductSerializer,StockSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # get all products Get
    def list(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"data":serializer.data,"success":"Fetch all Products"})
  
    # create a new product  POST
    def create(self, request, *args, **kwargs):
       name = request.data.get('name')
       description = request.data.get('description')
       price = request.data.get('price')
       category_id = request.data.get('category_id')

       try:
          if not name:
            return Response({"error": "Name is required"}, status=status.HTTP_400_BAD_REQUEST)
          
          if not price:
            return Response({"error": "price is required"}, status=status.HTTP_400_BAD_REQUEST)
          
          category = Category.objects.get(id=category_id)

          product=Product.objects.create(name=name,description=description,price=price,category=category)

          serializer = ProductSerializer(product)

          return Response({"data":serializer.data,"success":"Product create successfully"}, status=status.HTTP_201_CREATED)
       
       except Category.DoesNotExist:
          return Response({"error": "Category doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
       except Exception as e:
        return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
  
    # update all document Put Method
    def update(self, request, pk=None):
      try:
          product = Product.objects.get(pk=pk)

          # Get the updated data from the request
          name = request.data.get('name')
          description = request.data.get('description')
          price = request.data.get('price')
          category_id = request.data.get('category_id')

          # Validate required fields
          if not name:
              return Response({"error": "Name is required"}, status=status.HTTP_400_BAD_REQUEST)
          
          if not price:
              return Response({"error": "Price is required"}, status=status.HTTP_400_BAD_REQUEST)

        
          if category_id:
              try:
                  category = Category.objects.get(id=category_id)
                  product.category = category  
              except Category.DoesNotExist:
                  return Response({"error": "Category doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
   
          product.name = name
          product.description = description
          product.price = price
          
          product.save()

          serializer = ProductSerializer(product)
        
          return Response({"data":serializer.data,"success":"Product Update successfully"}, status=status.HTTP_200_OK)
      
      except Product.DoesNotExist:
          return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
      
      except Exception as e:
          return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    # update specfic document PATCH Method
    def partial_update(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)

            # Get the updated data from the request (fields are optional)
            name = request.data.get('name', product.name)
            description = request.data.get('description', product.description)
            price = request.data.get('price', product.price)
            category_id = request.data.get('category_id')

            if category_id:
              try:
                category = Category.objects.get(id=category_id)
                product.category = category
              except Category.DoesNotExist:
                return Response({"error": "Category doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)

            product.name = name
            product.description = description
            product.price = price

            product.save()

            serializer = ProductSerializer(product)

            return Response({"data":serializer.data,"success":"Product udated successfully"}, status=status.HTTP_200_OK)

        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    # delete product DELETE Method
    def destroy(self, request, *args, **kwargs):
        try:
          instance = self.get_object()
          self.perform_destroy(instance)
          return Response({"success": "Product delete successfully."}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class StockViewSet(viewsets.ModelViewSet):
  queryset = Stock.objects.all()
  serializer_class = StockSerializer

