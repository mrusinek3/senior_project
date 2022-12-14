from django import forms
from .models import Category, Product
from django.forms import HiddenInput

# Form used to create a new product in the inventory (requires the category, name, and quantity)
class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'item_name', 'quantity']
    
    # Validation Check
    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError('This field is required!')
        return category

    # Validation Check
    # Do not allow the creation of an already created product, no duplicates
    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')
        if not item_name:
            raise forms.ValidationError('This field is required!')
        for instance in Product.objects.all():
            if instance.item_name == item_name:
                raise forms.ValidationError(str(item_name) + " already exists, cannot duplicate!")
        return item_name

# Form used to updated a product in the inventory
class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'item_name', 'quantity']

    # Validation Check
    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError('This field is required!')
        return category

    # Validation Check
    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')
        if not item_name:
            raise forms.ValidationError('This field is required!')
        return item_name

# Form used to create a category in the inventory
class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']
    
    # Validation Check
    # Do not allow the creation of an already created category, no duplicates
    def clean_category_name(self):
        category = self.cleaned_data.get('category_name')
        if not category:
            raise forms.ValidationError('This field is required!')
        for instance in Category.objects.all():
            if instance.category_name == category:
                raise forms.ValidationError(str(category) + ' already exists, cannot duplicate!')
        return category

# Form used to update a category in the inventory
class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']

    # Validation Check
    def clean_category_name(self):
        category = self.cleaned_data.get('category_name')
        if not category:
            raise forms.ValidationError('This field is required!')
        return category

# Form used to set the reorder level for a given product (used to compare against product quantity to determine if product quantity is low)
class ProductReorderForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['reorder_level']

# Form used to issue a given amount of a certain product
class ProductIssueForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['issue_quantity', 'issue_to', 'quantity']
        widgets = {'quantity': forms.HiddenInput()}

# Form used to receive a given amount of a certain product
class ProductReceiveForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['receive_quantity', 'receive_by']



