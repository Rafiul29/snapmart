from django.db import models

# Create your models here.
class Category(models.Model):
  name=models.CharField(max_length=100,unique=True)

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name_plural = "categories"


class Product(models.Model):
  name=models.CharField(max_length=100)
  description=models.TextField(blank=True,null=True)
  price=models.DecimalField(max_digits=10,decimal_places=2)
  category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')

  def __str__(self):
    return self.name
  
  
  

class Stock(models.Model):
  product=models.OneToOneField(Product,on_delete=models.CASCADE,related_name='stock')
  quantity=models.PositiveIntegerField()

  def __str__(self):
    return f"{self.product.name} - {self.quantity}"