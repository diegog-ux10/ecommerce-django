from django.db import models
import uuid

class Product(models.Model):
    pid = models.CharField(max_length=255)  # Product ID
    name = models.CharField(max_length=100)  # Product Name
    slug = models.SlugField(max_length=100)  # Product Slug
    description = models.TextField()  # Product Description
    is_digital = models.BooleanField(default=False)  # Is Digital Product
    create_at = models.DateTimeField(auto_now_add=True)  # Create Date
    is_active = models.BooleanField(default=True)  # Is Active

class ProductLine(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Product Price
    sku = models.UUIDField(default=uuid.uuid4, editable=False)  # Product SKU
    stock_qty = models.IntegerField()
    is_active = models.BooleanField()
    order = models.IntegerField()
    weight = models.FloatField()

class ProductImage(models.Model):
    name = models.CharField(max_length=100)
    alternative_text = models.CharField(max_length=100)
    url = models.ImageField()
    
    
    
