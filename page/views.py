from django.db.models import Q
from django.shortcuts import render, redirect

from page.forms import CategoryForm, ProductForm
from page.models import Category, Product



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages


def product_search_view(request):
    query = request.GET.get('q')  # foydalanuvchi yozgan so‘z
    results = Product.objects.all()

    if query:
        results = results.filter(
            Q(name__icontains=query) |
            Q(category__name__icontains=query) |
            Q(description__icontains=query) |
            Q(price__icontains=query)
        )
    return render(request, 'products/product_list.html', {'products': results, 'query': query})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Ro‘yxatdan o‘tish muvaffaqiyatli yakunlandi. Xush kelibsiz!")
            return redirect('category-list')
        else:
            messages.error(request, "Ro‘yxatdan o‘tish muvaffaqiyatsiz yakunlandi. Iltimos, formadagi xatolarni tekshirib ko‘ring.")
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def get_category(request):
    cat = Category.objects.all()
    return render(request, 'products/category.html', {'cat':cat})


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('category-list')
    else:
        form = CategoryForm()
    return render(request, 'products/category_form.html', {'form':form})


def detail_category(request, pk):
    cat = Category.objects.get(pk=pk)
    return render(request, 'products/category_detail.html', {'cat':cat})


def delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'POST':
        category = Category.objects.get(pk=pk)
        category.delete()
        return redirect('category-list')
    return render(request, 'products/delete_category.html', {'category':category})



def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products':products})




def create_product(request):
    form=ProductForm(request.POST or None)
    if request.method == 'POST':
        form=ProductForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('product-list')
        form = ProductForm(request.POST or None)
    return render(request, 'products/product_form.html', {'form':form})

def detail_pro(request, pk):
    pro = Product.objects.get(pk=pk)
    return render(request, 'products/product_detail.html', {'pro':pro})


def delete_pro(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product = Product.objects.get(pk=pk)
        product.delete()
        return redirect('category-list')
    return render(request, 'products/delete_pro.html', {'product':product})

def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form})



def get_non(request):
    return render(request, 'products/product_form.html', {'form': form})

