from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db import models
from .models import Post, FunFact, Category

def front(request):
    return render(request, 'blog/front.html')


def home(request):
    template_name = 'blog/home.html'
    include_other = True
    context = {
        'template_name' : template_name,
        'posts' : Post.objects.all().order_by('animal'),
        'include_other' : include_other
    }   
    return render(request, template_name, context)

def sort_animals(request, animal_type=None):
    if animal_type:
        sort_query = Post.objects.filter(an_type = animal_type)
    else:
        sort_query = Post.objects.all()
        sci_name = sort_query.values_list('sci_name', flat=True)
        fav_food = sort_query.values_list('fav_food', flat=True)
        animal_cat = sci_name = sort_query.values_list('animal_cat', flat=True)
    context1 = {
        'posts' : sort_query,
        'selected_animal_type' : animal_type,
    }
    return render(request, 'blog/sorting.html', context1)

def sort_animals_type(request, animal_type=None):
    include_other = False
    if animal_type:
        sort_query = Post.objects.filter(an_type = animal_type)
    else:
        sort_query = Post.objects.all()
    context = {
        'posts' : sort_query,
        'selected_animal_type' : animal_type,
        'inlude_other' : include_other
    }   
    return render(request, 'blog/sorting_clicked.html', context)

def classification(request):
    categories = Category.objects.all()
    return render(request, 'blog/classification.html', {'categories': categories})

def funfacts(request):
    random_fact = FunFact.objects.order_by('?').first()

    context = { 
        'random_fact' : random_fact
    }
    return render(request, 'blog/fun-facts.html', context)

def search(request):
    search_query = request.GET.get('search_query', '')
    if not search_query:
        return redirect('blog:blog-home')
    search_results = Post.objects.filter(
        models.Q(an_type__icontains = search_query) |
        models.Q(animal__icontains = search_query) |
        models.Q(definition__icontains = search_query) |
        models.Q(location_discovered__icontains = search_query) |
        models.Q(location__icontains = search_query) |
        models.Q(more_info__icontains = search_query    )
        )
    return render(request, 'blog/search.html', {'search_query' : search_query, 'search_results' : search_results})

def clicked_info(request, animal_name):
    
    post = get_object_or_404(Post, animal=animal_name)
    return render(request, 'blog/clicked_info.html', {'post': post}) 