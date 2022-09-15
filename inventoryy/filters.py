import django_filters
from .models import *
from django_filters import CharFilter, NumberFilter, OrderingFilter, DateFilter, DateRangeFilter, DateFromToRangeFilter
from django_filters.widgets import RangeWidget


class ProductFilter(django_filters.FilterSet):
    item_name = CharFilter(required=False, field_name='item_name', lookup_expr='contains', label='Item Name')
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

class ProductHistoryFilter(django_filters.FilterSet):
    item_name = CharFilter(required=False, field_name='item_name', lookup_expr='icontains', label='Item Name')
    date_range = DateRangeFilter(field_name="last_updated", label="Date")
    date = DateFromToRangeFilter(field_name="last_updated",label="Date Range (Start - End)", widget=RangeWidget(attrs={'type': 'date'}))

    class Meta:
        model = Product
        fields = ['category', 'item_name']

class ProductCountFilter(django_filters.FilterSet):
    item_name = CharFilter(required=False, field_name='item_name', lookup_expr='icontains', label='Item Name')
    quantity = NumberFilter(required=False, field_name='quantity', lookup_expr='lte', label='Quantity')

    class Meta:
        model = Product
        fields = ['category', 'item_name', 'quantity']