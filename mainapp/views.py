from django.shortcuts import render

from mainapp.models import Product, Category


def index(request):
    title = 'Главная'

    prods = Product.objects.all()[:4]

    context = {
        'title': title,
        'products': prods,
    }


    return render(request, 'index.html', context)

def contacts(request):
    title = 'Контакты'

    context = {
        'title': title,
    }
    return render(request, 'contact.html')

def about(request):
    title = 'О нас'

    context = {
        'title': title,
    }
    return render(request, 'about.html')

def products(request):
    title = 'Продукты'
    prods = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'title': title,
        'products': prods,
        'categories': categories,
    }
    return render(request, 'products.html', context)

def product(request):
    title = 'Продукты'

    prod = Product.objects.get(id=1)

    context = {
        'title': title,
        'product': prod,
    }
    return render(request, 'product.html', context)
