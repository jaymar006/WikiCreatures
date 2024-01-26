from django.contrib import admin
from .models import Post, FunFact, Category

admin.site.register(Post)
admin.site.register(FunFact)
admin.site.register(Category)
