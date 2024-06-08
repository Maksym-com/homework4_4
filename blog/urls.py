from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('product/<int:product_id>/', views.products, name='products'),
    path('heroes/', views.heroes, name='heroes'),
    path('heroes/<int:hero_id>/', views.hero_detail, name='hero_detail'),
    path('salut/', views.salut, name='salut')
]