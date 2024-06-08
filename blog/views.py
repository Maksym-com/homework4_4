from django.http import HttpResponse
from django.shortcuts import render

menu = ['home', 'about', 'posts']
items = {
    'Smartphone': {
    'id': 1,
    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    },
        'Laptop': {
        'id': 2,
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    },
        'Keyboard': {
        'id': 3,
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    },
        'Mouse': {
        'id': 4,
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    }
}

main_heroes = {
    'Anankin Skywalker': {
    'id': 1,
    'description': 'The chosen one'
    },
        'Obi-Wan Kenobi': {
        'id': 2,
        'description': 'Hello there!'
    },
        'Luke Skywalker': {
        'id': 3,
        'description': 'Son of Anakin'
    },
        'Leia Organa': {
        'id': 4,
        'description': 'Sister of Luke'
    },
    'Yoda': {
        'id': 5,
        'description': 'The Great Jedi'
    }
}

def home(request):
    data = {
        'menu': menu,
        'products': items
    }
    return render(request, 'blog/index.html', context=data)

def heroes(request):
    return render(request, 'blog/heroes.html', context={'main_heroes': main_heroes.items()})

def hero_detail(request, hero_id):
    heroes = [i for i in main_heroes if main_heroes[i]['id'] == hero_id]
    return render(request, 'blog/hero_detail_view.html', {'hero': main_heroes[heroes[0]]})

def products(request, product_id):
    product_lst = [i for i in items if items[i]['id'] == product_id]
    return render(request, 'blog/product.html', {'product_desc': items[product_lst[0]]})

def salut(request):
    return render(request, 'blog/salut.html')

def about(request):
    return render(request, 'blog/about.html')
