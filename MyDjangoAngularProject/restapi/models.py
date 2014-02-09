from django.db import models

# Create your models here.
class Album(models.Model):
	name = models.CharField(max_length=200)
	
	def __str__(self):  # Python 3: def __str__(self):
		return self.name

class Photo(models.Model):
	url = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	album = models.ForeignKey(Album)

	def __str__(self):  # Python 3: def __str__(self):
		return self.name

