from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.front, name="blog-front"),
    path('Home/', views.home, name = 'blog-home'),
    path('classification/', views.classification, name = 'blog-classification'),
    path('fun-facts/', views.funfacts, name = 'blog-funfacts'),
    path('Sorted/<str:animal_type>/', views.sort_animals, name='blog-animals'),
    path('Sorted-link/<str:animal_type>/', views.sort_animals_type, name='blog-animals2'),
    path('Animal/<str:animal_name>', views.clicked_info, name='blog-info'),
    path('Search/', views.search, name='blog-search'),
]