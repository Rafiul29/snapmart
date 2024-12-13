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

  # get all Category Get Method
  def list(self, request, *args, **kwargs):
      queryset = Category.objects.all()
      serializer = self.get_serializer(queryset, many=True)
      return Response({"data":serializer.data,"success":"Fetch all Categories"})
    #  get single product Get Method
  
  # get single Category Get Method
  def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            product = Category.objects.get(pk=pk)
            serializer = self.get_serializer(product)

            return Response(
                {"data": serializer.data, "success": "Fetch single Category successfully"}, 
                status=status.HTTP_200_OK
            )
        
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

  # create a new Category  POST Method
  def create(self, request, *args, **kwargs):
       name = request.data.get('name')

       try:
          if not name:
            return Response({"error": "Category name is required"}, status=status.HTTP_400_BAD_REQUEST)
          
          catetory=Category.objects.create(name=name)

          serializer = CategorySerializer(catetory)

          return Response({"data":serializer.data,"success":"Category create successfully"}, status=status.HTTP_201_CREATED)
       
       except Exception as e:
        return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
  
  # update all  document Put Method
  def update(self, request, pk=None):
      try:
          category = Category.objects.get(pk=pk)

          # Get the updated data from the request
          name = request.data.get('name')

          # Validate required fields
          if not name:
            return Response({"error": "Category name is required"}, status=status.HTTP_400_BAD_REQUEST)

          category.name = name
          category.save()

          serializer = CategorySerializer(category)
        
          return Response({"data":serializer.data,"success":"Category Update successfully"}, status=status.HTTP_200_OK)
      
      except Exception as e:
          return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    # delete product DELETE Method
  
  # delete Category DELETE Method
  def destroy(self, request, *args, **kwargs):
    try:
      instance = self.get_object()
      self.perform_destroy(instance)
      return Response({"success": "Category delete successfully."}, status=status.HTTP_200_OK)
    except Category.DoesNotExist:
      return Response({"error": "Category not found."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
      return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # get all products Get Method
    def list(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"data":serializer.data,"success":"Fetch all Products"})
   
    # get single product Get Method
    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            product = Product.objects.get(pk=pk)
            serializer = self.get_serializer(product)

            return Response(
                {"data": serializer.data, "success": "Fetch single product successfully"}, 
                status=status.HTTP_200_OK
            )
        
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    # create a new product  POST Method
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

  # get all Stocks Product Get Method
  def list(self, request, *args, **kwargs):
      queryset = Stock.objects.all()
      serializer = self.get_serializer(queryset, many=True)
      return Response({"data":serializer.data,"success":"Fetch all Stocks Product"})

  # get single Stock Product Get Method
  def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            product = Stock.objects.get(pk=pk)
            serializer = self.get_serializer(product)

            return Response(
                {"data": serializer.data, "success": "Fetch single Stock Product successfully"}, 
                status=status.HTTP_200_OK
            )
        
        except Stock.DoesNotExist:
            return Response({"error": "Product Stock  not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    # create a new product  POST Method
  
  # create new  product stock POST Method 
  def create(self, request, *args, **kwargs):
       quantity = request.data.get('quantity')
       product_id = request.data.get('product_id')

       try:
          if not quantity:
            return Response({"error": "Quantity is required"}, status=status.HTTP_400_BAD_REQUEST)
          
          product = Product.objects.get(id=product_id)

          stock=Stock.objects.create(quantity=quantity,product=product)

          serializer = StockSerializer(stock)

          return Response({"data":serializer.data,"success":"Stock Product create successfully"}, status=status.HTTP_201_CREATED)
       
       except Product.DoesNotExist:
          return Response({"error": "Product doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
       except Exception as e:
        return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
       
    # update all document Put Method
  
  # update product stock PUT Method
  def update(self, request, pk=None):
      try:
          stock = Stock.objects.get(pk=pk)

          # Get the updated data from the request
          quantity = request.data.get('quantity')
          product_id = request.data.get('product_id')

          # Validate required fields
          if not quantity:
              return Response({"error": "Quantity is required"}, status=status.HTTP_400_BAD_REQUEST)

          if product_id:
              try:
                  product = Product.objects.get(id=product_id)
                  stock.product = product  
              except Product.DoesNotExist:
                  return Response({"error": "Category doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
   
          stock.quantity = quantity
  
          stock.save()

          serializer = StockSerializer(stock)
        
          return Response({"data":serializer.data,"success":"Product Stock Update successfully"}, status=status.HTTP_200_OK)
      
      except Stock.DoesNotExist:
          return Response({"error": "Product Stock not found"}, status=status.HTTP_404_NOT_FOUND)
      
      except Exception as e:
          return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

  # update specifc field PAtch Method
  def partial_update(self, request, pk=None):
        try:
            stock = Stock.objects.get(pk=pk)

            # Get the updated data from the request (fields are optional)
            quantity = request.data.get('quantity',stock.quantity)
            product_id = request.data.get('product_id')
          
            if product_id:
              try:
                  product = Product.objects.get(id=product_id)
                  stock.product = product  
              except Product.DoesNotExist:
                  return Response({"error": "Product  doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
   
            stock.quantity=quantity

            stock.save()

            serializer = StockSerializer(stock)

            return Response({"data":serializer.data,"success":"Product Stock  udated successfully"}, status=status.HTTP_200_OK)

        except Stock.DoesNotExist:
            return Response({"error": "Product Stock not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    # delete product DELETE Method
  
  # delete product stock DELETE Method
  def destroy(self, request, *args, **kwargs):
        try:
          instance = self.get_object()
          self.perform_destroy(instance)
          return Response({"success": "Product Stock delete successfully."}, status=status.HTTP_200_OK)
        except Stock.DoesNotExist:
            return Response({"error": "Product Stock  not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        