from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MinValueValidator

# Create your models here.

# Database Model used to store the information pertaining to a Category
class Category(models.Model):
    category_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.category_name

# Database Model used to store the information pertaining to a Product
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    item_name = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=True, null=True, validators=[MinValueValidator(0)])
    receive_quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_by = models.CharField(max_length=100, blank=True, null=True)
    issue_quantity = models.IntegerField(default='0', blank=True, null=True)
    issue_by = models.CharField(max_length=100, blank=True, null=True)
    issue_to = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    reorder_level = models.IntegerField(default='0', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return self.item_name

# Database Model used to store the usage history of information all products (adds a row of data everytime a product is issued or received)
class ProductHistoryLog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    item_name = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=True, null=True, validators=[MinValueValidator(0)])
    receive_quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_by = models.CharField(max_length=100, blank=True, null=True)
    issue_quantity = models.IntegerField(default='0', blank=True, null=True)
    issue_by = models.CharField(max_length=100, blank=True, null=True)
    issue_to = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    reorder_level = models.IntegerField(default='0', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
    date_created = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)

    def __str__(self):
        return self.item_name
    