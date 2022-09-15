import django_filters
from .models import *
from django_filters import CharFilter, NumberFilter, OrderingFilter, DateFilter, DateRangeFilter, DateFromToRangeFilter
from django_filters.widgets import RangeWidget

# Filters used to filter the data within the table

# Filter we see in the List of Products page
# Quantity filters the quantity by those less than the inputted value
# Item name filters the item names based off the inputted characters, case insensitive
# Sorting takes in 4 choices fields (filter quantity ascending, filter quantity descending, filter date ascending, filter date descending)
class ProductFilter(django_filters.FilterSet):

    item_name = CharFilter(required=False, field_name='item_name', lookup_expr='icontains', label='Item Name')
    quantity = NumberFilter(required=False, field_name='quantity', lookup_expr='lte', label='Quantity')

    sorting = OrderingFilter(
        label="Sort",
        required = False,
        choices=(
            ('ascending quantity', 'Quantity Low to High'),
            ('descending quantity', 'Quantity High to Low'),
            ('ascending date created', 'Date Created Old to New'),
            ('descending date created', 'Date Created New to Old'),
        ),
        fields={
            'quantity': 'ascending quantity',
            '-quantity': 'descending quantity',
            'date_created': 'ascending date created',
            '-date_created': 'descending date created',
        },
    )

    class Meta:
        model = Product
        fields = ['category', 'item_name', 'quantity']

# Filter we see in the Products Usage History page
# Item name filters the item names based off the inputted characters, case insensitive
# DateRangeFilter provides 5 ranges of dates to filter with (today, yesterday, last week, last month, last year)
class ProductHistoryFilter(django_filters.FilterSet):
    item_name = CharFilter(required=False, field_name='item_name', lookup_expr='icontains', label='Item Name')
    date_range = DateRangeFilter(field_name="last_updated", label="Date")
    date = DateFromToRangeFilter(field_name="last_updated",label="Date Range (Start - End)", widget=RangeWidget(attrs={'type': 'date'}))

    class Meta:
        model = Product
        fields = ['category', 'item_name']

# Filter we see in the Product Count pages
# Quantity filters the quantity by those less than the inputted value
# Item name filters the item names based off the inputted characters, case insensitive
class ProductCountFilter(django_filters.FilterSet):
    item_name = CharFilter(required=False, field_name='item_name', lookup_expr='icontains', label='Item Name')
    quantity = NumberFilter(required=False, field_name='quantity', lookup_expr='lte', label='Quantity')

    class Meta:
        model = Product
        fields = ['category', 'item_name', 'quantity']