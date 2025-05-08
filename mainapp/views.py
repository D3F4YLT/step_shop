from django.shortcuts import render

def index(request):
    title = 'Главная'

    context = {
        'title': title,
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

    context = {
        'title': title,
    }
    return render(request, 'products.html')

def product(request):
    title = 'Продукты'

    context = {
        'title': title,
    }
    return render(request, 'product.html')
