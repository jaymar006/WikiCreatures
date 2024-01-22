from django.db import models
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver

class Post(models.Model):
	an_type = models.CharField(max_length=100)
	animal_cat = models.CharField(max_length=50)
	animal = models.CharField(max_length=100)
	definition = models.TextField()
	date_discovered = models.CharField(max_length=100)
	discovered_by = models.CharField(max_length=100)
	more_info = models.TextField(null=True, blank=True)
	image_name = models.CharField(max_length=50)
	image = models.ImageField(upload_to="img/%y", height_field=None, width_field=None, max_length=None)


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