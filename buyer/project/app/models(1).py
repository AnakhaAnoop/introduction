from django.db import models

# Create your models here.

class product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    
    
    def __str__(self):
        return self.product_name
    
    
class Buyer(models.Model):
    product = models.ForeignKey(product,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name 
    
    
    
    
    
    
    