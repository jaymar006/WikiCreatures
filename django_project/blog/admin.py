from django.contrib import admin
from .models import Post, FunFact, Category, Category_informations

admin.site.register(Post)
admin.site.register(FunFact)
admin.site.register(Category)
admin.site.register(Category_informations)