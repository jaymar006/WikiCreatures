from django.db import models
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

class Post(models.Model):
	an_type = models.CharField(max_length=100)
	animal_cat = models.CharField(max_length=50)
	animal = models.CharField(max_length=100)
	definition = models.TextField()
	location_discovered = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	more_info = models.TextField(null=True, blank=True)
	image_name = models.CharField(max_length=50)
	image = models.ImageField(upload_to="img/%y", height_field=None, width_field=None, max_length=None)
	sci_name = models.CharField(max_length=255)
	fav_food = models.CharField(max_length=255)



	def __str__(self):
		return self.animal
	
	def __str__(self):
		return self.image_name
	
class FunFact(models.Model):
	animal = models.CharField(max_length=255)
	fact = models.TextField()
	image = models.ImageField(upload_to="img/%y", height_field=None, width_field=None, max_length=None)

	def __str__(self):
		return self.animal


class Category(models.Model):
    categories_type = models.CharField(max_length=255)
    categories_description = models.TextField()
    category_image = models.ImageField(upload_to='category_images/%y')

    def __str__(self):
        return self.categories_type
	

class Category_informations(models.Model):
    categories_type = models.CharField(max_length=255)
    categories_description = models.TextField()
    category_image = models.ImageField(upload_to='category_images/%Y')
    image_one = models.ImageField(upload_to='category_images/catview_images/%Y', blank=True, null=True)
    image_two = models.ImageField(upload_to='category_images/catview_images/%Y', blank=True, null=True)
    image_three = models.ImageField(upload_to='category_images/catview_images/%Y', blank=True, null=True)
    image_four = models.ImageField(upload_to='category_images/catview_images/%Y', blank=True, null=True)
    image_five = models.ImageField(upload_to='category_images/catview_images/%Y', blank=True, null=True)
    image_six = models.ImageField(upload_to='category_images/catview_images/%Y', blank=True, null=True)
    characteristics = models.TextField()
    habitat = models.TextField()
    diet = models.TextField()
    reproduction = models.TextField()
    notable_species = models.TextField()

    def __str__(self):
        return self.categories_type