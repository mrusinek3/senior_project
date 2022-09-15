from django.contrib import admin
from .models import Product, Category, ProductHistoryLog
from .forms import ProductCreateForm

#Modifies how the product model is displayed in the database
#Instead of just showing the name, it now shows the name, category, and quantity
class ProductCreateAdmin(admin.ModelAdmin):
   list_display = ['id', 'category', 'item_name', 'quantity', 'date_created', 'last_updated']
   form = ProductCreateForm
   list_filter = ['category']
   search_fields = ['category', 'item_name']

# Register your models here.
admin.site.register(Product, ProductCreateAdmin)
admin.site.register(Category)
admin.site.register(ProductHistoryLog)