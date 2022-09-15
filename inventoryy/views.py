from django.shortcuts import render, redirect
from .models import Product, Category, ProductHistoryLog
from .forms import ( ProductCreateForm, ProductUpdateForm, CategoryCreateForm, CategoryUpdateForm, 
                     ProductIssueForm, ProductReceiveForm, ProductReorderForm)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import csv
from .filters import ProductFilter, ProductHistoryFilter, ProductCountFilter
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.db.models import Sum, Count

# Create your views here.

# function view for the administration panel
@login_required
def admin_panel(request):
    products = Product.objects.all().order_by('id')
    product_count = Product.objects.all().count()
    category_count = Category.objects.all().count()
    user_count = User.objects.all().count()
    quantity_count = Product.objects.all().aggregate(data=Sum('quantity'))
    paginate = Paginator(products, 5)
    page = request.GET.get('page')
    products_list = paginate.get_page(page)

    context = {
        "Title": "Admin Panel",
        "products": products,
        "products_list": products_list,
        "product_count": product_count,
        "category_count": category_count,
        "user_count": user_count,
        "quantity_count": quantity_count,
    }
    return render(request, 'inventoryy/admin_panel.html', context)

# function based view for the employee panel
@login_required
def employee_panel(request):
    products = Product.objects.all().order_by('id')
    product_count = Product.objects.all().count()
    category_count = Category.objects.all().count()
    user_count = User.objects.all().count()
    quantity_count = Product.objects.all().aggregate(data=Sum('quantity'))
    paginate = Paginator(products, 5)
    page = request.GET.get('page')
    products_list = paginate.get_page(page)

    context = {
        "Title": "Employee Panel",
        "products": products,
        "products_list": products_list,
        "product_count": product_count,
        "category_count": category_count,
        "user_count": user_count,
        "quantity_count": quantity_count,
    }
    return render(request, 'inventoryy/employee_panel.html', context)

# function based view for the about page
def about(request):
    return render(request, 'inventoryy/about.html', { "title": "about"})

# function based view that displays a table of all the products with their corresponding details that are within the database
@login_required
def list_products(request):
    all_products = Product.objects.all().order_by('id')
    filters = ProductFilter(request.GET, queryset=all_products)
    paginate = Paginator(filters.qs, 4)
    page = request.GET.get('page')
    products_list = paginate.get_page(page)

    context = {
        "filters": filters,
        "products_list": products_list,
        "title": "Product List",
    }

    return render(request, 'inventoryy/list_products.html', context)

# function based view that displays a form to add a product to the database
@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            form.save()
            product = form.cleaned_data.get('item_name')
            quantity = form.cleaned_data.get('quantity')
            messages.success(request, f'Sucessfully created {quantity} {product}s!')
            return redirect('admin-panel')
    else:
        form = ProductCreateForm()

    context = {
        "form": form,
        "title": "Add Product",
    }

    return render(request, "inventoryy/add_product.html", context)

# function based view that displays a form to update an existing product
@login_required
def update_product_form(request, pk):
    all_products = Product.objects.get(id=pk)
    form = ProductUpdateForm(instance=all_products)
    
    if request.method == 'POST':
        form = ProductUpdateForm(request.POST, instance=all_products)
        if form.is_valid():
            form.save()
            product = form.cleaned_data.get('item_name')
            messages.success(request, f'Sucessfully Updated {product}!')
            return redirect('update-product')

    context = {
        'form':form,
        "title":"Update Product",
	}

    return render(request, 'inventoryy/update_product_form.html', context)

# function based view that displays a table of all the products with the option to update a given product
@login_required
def update_product(request):
    all_products = Product.objects.all().order_by('category')
    paginate = Paginator(all_products, 4)
    page = request.GET.get('page')
    products_list = paginate.get_page(page)


    context = {
        "products": all_products,
        "products_list": products_list,
        "title": "Update Product",
    }

    return render(request, 'inventoryy/update_product.html', context)

# function based view that displays a table of all the products with the option to delete a given product
@login_required
def delete_product(request):
    all_products = Product.objects.all().order_by('category')
    paginate = Paginator(all_products, 4)
    page = request.GET.get('page')
    products_list = paginate.get_page(page)

    context = {
        "products": all_products,
        "products_list": products_list,
        "title": "Delete Product",
    }

    return render(request, 'inventoryy/delete_product.html', context)

# function based view that displays message to confirm deleltion of currently selected product
@login_required
def confirm_delete_product(request, pk):
    all_products = Product.objects.get(id=pk)

    if request.method == 'POST':
        all_products.delete()
        messages.success(request, 'Successfully Deleted Product!')
        return redirect('all-products')
    
    context = {
        "all_products": all_products,
        "title": "Delete Product",
    }

    return render(request, 'inventoryy/confirm_delete_product.html', context)

# function based view that displays all the current categories in the inventory
@login_required
def list_category(request):
    all_categories = Category.objects.all()
    paginate = Paginator(all_categories, 2)
    page = request.GET.get('page')
    category_list = paginate.get_page(page)

    context = {
        "categories": all_categories,
        "category_list": category_list,
        "title": "All Categories",
    }

    return render(request, 'inventoryy/list_category.html', context)

# function based view that displays a form to add a category to the inventory
@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            category_name = form.cleaned_data.get('category_name')
            messages.success(request, f'Sucessfully Created Category: {category_name}!')
            return redirect('admin-panel')
    else:
        form = CategoryCreateForm()

    context = {
        "form": form,
        "title": "Add Category",
    }

    return render(request, "inventoryy/add_category.html", context)

# function based view that displays a table of all the categories with the option to delete a given category
@login_required
def delete_category(request):
    all_categories = Category.objects.all()
    paginate = Paginator(all_categories, 2)
    page = request.GET.get('page')
    category_list = paginate.get_page(page)

    context = {
        "categories": all_categories,
        "category_list": category_list,
        "title": "Delete Category",
    }

    return render(request, 'inventoryy/delete_category.html', context)

# function based view that displays message to confirm deleltion of currently selected category
@login_required
def confirm_delete_category(request, pk):
    all_categories = Category.objects.get(id=pk)

    if request.method == 'POST':
        all_categories.delete()
        messages.success(request, f'Successfully Deleted Category!')
        return redirect('all-categories')
    
    context = {
        "all_categories": all_categories,
        "title": "Delete Category",
    }

    return render(request, 'inventoryy/confirm_delete_category.html', context)

# function based view that displays a form to update an existing category
@login_required
def update_category_form(request, pk):
    all_categories = Category.objects.get(id=pk)
    form = CategoryUpdateForm(instance=all_categories)
    
    if request.method == 'POST':
        form = CategoryUpdateForm(request.POST, instance=all_categories)
        if form.is_valid():
            form.save()
            category = form.cleaned_data.get('category_name')
            messages.success(request, f'Sucessfully Updated {category}!')
            return redirect('update-category')

    context = {
        'form':form,
        "title":"Update Category",
	}

    return render(request, 'inventoryy/update_category_form.html', context)

# function based view that displays a table of all the categories with the option to update a given product
@login_required
def update_category(request):
    all_categories = Category.objects.all()
    paginate = Paginator(all_categories, 2)
    page = request.GET.get('page')
    category_list = paginate.get_page(page)

    context = {
        "categories": all_categories,
        "category_list": category_list,
        "title": "Update Category",
    }

    return render(request, 'inventoryy/update_category.html', context)

# function based view that will automatically export the current inventory to a CSV file
@login_required
def export_inventory(request):
    all_products = Product.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Current_Inventory.csv"'   
    writer = csv.writer(response)
    writer.writerow(['CATEGORY', 'PRODUCT NAME', 'QUANTITY'])

    instance = all_products
    for product in instance:
        writer.writerow([product.category, product.item_name, product.quantity])
    return response

# function based view that will automatically export the current usage history to a CSV file
@login_required
def export_usage_history(request):
    all_products = ProductHistoryLog.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Usage_History.csv"'   
    writer = csv.writer(response)
    writer.writerow(['CATEGORY', 'ITEM NAME', 'QUANTITY', 'ISSUE QUANTITY', 'RECEIVE QUANTITY', 'RECEIVE BY', 'ISSUE BY', 'LAST UPDATED'])
    instance = all_products
    for product in instance:
        writer.writerow([product.category, product.item_name, product.quantity, product.issue_quantity, product.receive_quantity, product.receive_by, product.issue_by, product.last_updated])
    return response

# function based view that will display the details of a single product
@login_required
def product_detail(request, pk):
    all_products = Product.objects.filter(id=pk)

    context = {
        "all_products": all_products,
        "title": "Update Category",
    }

    return render(request, 'inventoryy/product_detail.html', context)

# function based view that allows the administrator to issue a certain amount of product to a user
@login_required
def issue_product(request, pk):
    all_products = Product.objects.get(id=pk)
    form = ProductIssueForm(request.POST or None, instance=all_products)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.quantity -= instance.issue_quantity
        instance.issue_by = str(request.user)
        messages.success(request, "Successfully Issued: " + str(instance.issue_quantity) + " " + str(instance.item_name) + "s! " + str(instance.quantity) +  " Remaining in Inventory.")
        instance.save()

        issue_history_log = ProductHistoryLog(
            category = instance.category,
            item_name = instance.item_name,
            quantity = instance.quantity,
            issue_quantity = instance.issue_quantity,
            issue_to = instance.issue_to,
            issue_by = instance.issue_by,
            last_updated = instance.last_updated
        )

        issue_history_log.save()
        
        return redirect('/products/' + str(instance.id))
        
    context = {
		"title": 'Issue ' + str(all_products.item_name),
		"all_products": all_products,
		"form": form,
        "username": "Issue By: " + str(request.user),
	}
    
    return render(request, "inventoryy/issue_product.html", context)


# function based view that allows the administrator to receive a certain amount of products
@login_required
def receive_product(request, pk):
    all_products = Product.objects.get(id=pk)
    form = ProductReceiveForm(request.POST or None, instance=all_products)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.quantity += instance.receive_quantity
        messages.success(request, "Successfully Received: " + str(instance.receive_quantity) + " " + str(instance.item_name) + "s! " + str(instance.quantity) +  " Now in Inventory.")
        instance.save()
        
        receive_history_log = ProductHistoryLog(
            category = instance.category,
            item_name = instance.item_name,
            quantity = instance.quantity,
            receive_quantity = instance.receive_quantity,
            receive_by = instance.receive_by,
            last_updated = instance.last_updated
        )

        receive_history_log.save()

        return redirect('/products/' + str(instance.id))
    
    context = {
			"title": 'Receive ' + str(all_products.item_name),
			"all_products": all_products,
			"form": form,
            "username": " By: " + str(request.user),
		}
    
    return render(request, "inventoryy/receive_product.html", context)

# function based view that controls the level at which a specific product should be re-ordered
@login_required
def reorder_product(request, pk):
    all_products = Product.objects.get(id=pk)
    form = ProductReorderForm(request.POST or None, instance=all_products)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Reorder Level For " + str(instance.item_name) + " Successfully Set To " + str(instance.reorder_level))
        
        return redirect('/products')

    context = {
            "title": "Set Product Reorder Level",
			"all_products": all_products,
			"form": form,
		}

    return render(request, "inventoryy/reorder_product.html", context)

# function based view that displays a table containing all of the products history
@login_required
def product_history(request):
    products = ProductHistoryLog.objects.all().order_by('category')
    filters = ProductHistoryFilter(request.GET, queryset=products)
    paginate = Paginator(filters.qs, 5)
    page = request.GET.get('page')
    history_list = paginate.get_page(page)

    context = {
        "Title": "Product History Log",
        "products": products,
        "history_list": history_list,
        "filters": filters,
    }

    return render(request, "inventoryy/product_history.html", context)

# function based view that calculates the total number of products in the inventory, 
# along with the total number of products in each category, then displays them in a table
@login_required
def total_products_quantity(request):
    all_products = Product.objects.all().aggregate(data=Sum('quantity'))
    categories = Category.objects.all().annotate(items_count=Count('product'))

    context = {
        "all_products": all_products,
        "title": "Delete Product",
        "categories": categories,
    }

    return render(request, 'inventoryy/all_quantity_sum.html', context)

# function based view displays a table with the count of each individual product
@login_required
def single_product_quantity(request):
    all_products = Product.objects.all().order_by('category')
    filters = ProductCountFilter(request.GET, queryset=all_products)
    paginate = Paginator(filters.qs, 4)
    page = request.GET.get('page')
    products_list = paginate.get_page(page)

    context = {
        "filters": filters,
        "products_list": products_list,
        "title": "Product List",
    }

    return render(request, 'inventoryy/single_product_count.html', context)

# function based view that displays a table containing all registered users on the application
@login_required
def display_users(request):
    all_users = User.objects.all().order_by("id")
    paginate = Paginator(all_users, 4)
    page = request.GET.get('page')
    users_list = paginate.get_page(page)

    context = {
        "all_users": all_users,
        "title": "Delete Product",
        "users_list": users_list,
    }

    return render(request, 'inventoryy/user_detail.html', context)

# function based view that displays a table of all the categories with the option to delete a given user
@login_required
def delete_user(request):
    all_users = User.objects.all().order_by("id")
    paginate = Paginator(all_users, 4)
    page = request.GET.get('page')
    users_list = paginate.get_page(page)

    context = {
        "all_users": all_users,
        "users_list": users_list,
        "title": "Delete Category",
    }

    return render(request, 'inventoryy/delete_user.html', context)

# function based view that displays message to confirm deleltion of currently selected user
@login_required
def confirm_delete_user(request, pk):
    all_users = User.objects.get(id=pk)

    if request.method == 'POST':
        all_users.delete()
        messages.success(request, f'Successfully Deleted User!')
        return redirect('accounts-list')
    
    context = {
        "all_users": all_users,
        "title": "Delete User",
    }

    return render(request, 'inventoryy/confirm_delete_user.html', context)