from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name="users/login.html", redirect_authenticated_user=True), name='login'),
    path('dashboard/admin/', views.admin_panel, name='admin-panel'),
    path('dashboard/employee/', views.employee_panel, name='employee-panel'),
    path('about/', views.about, name='inventory-about'),
    path('export/', views.export_inventory, name="export-to-csv"),
    path('users/', views.display_users, name='accounts-list'),
    path('users/delete', views.delete_user, name='account-delete'),
    path('users/delete/<str:pk>/', views.confirm_delete_user, name='confirm-delete-user'),
    path('history/', views.product_history, name="product-history-log"),
    path('history/export/', views.export_usage_history, name="export-usage-to-csv"),
    path('products/', views.list_products, name='all-products'),
    path('products/add/', views.add_product, name='add-product'),
    path('products/update/<str:pk>/', views.update_product_form, name='update-product-form'),
    path('products/update', views.update_product, name='update-product'),
    path('products/delete/<str:pk>/', views.confirm_delete_product, name="confirm-delete-product"),
    path('products/delete/', views.delete_product, name="delete-product"),
    path('products/<str:pk>/', views.product_detail, name="single-product"), 
    path('products/issue/<str:pk>/', views.issue_product, name="issue-product"), 
    path('products/receive/<str:pk>/', views.receive_product, name="receive-product"), 
    path('products/reorder/<str:pk>/', views.reorder_product, name="reorder-product"), 
    path('products/quantity/sum', views.total_products_quantity, name="products-quantity-sum"), 
    path('products/quantity/single/', views.single_product_quantity, name="single-product-quantity"), 
    path('categories/', views.list_category, name="all-categories"),
    path('category/add/', views.add_category, name="add-category"),
    path('category/delete/', views.delete_category, name="delete-category"),
    path('category/delete/<str:pk>/', views.confirm_delete_category, name="confirm-delete-category"),
    path('category/update/', views.update_category, name="update-category"),
    path('category/update/<str:pk>/', views.update_category_form, name="update-category-form"),
]