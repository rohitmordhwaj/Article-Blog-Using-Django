from django.db import models

# Create your models here.
class Article(models.Model):
	title=models.CharField(max_length=200)
	slug=models.SlugField()
	body=models.TextField()
	time=models.DateTimeField(auto_now_add=True)
	thumb=models.ImageField(default='default.png',blank=True)

	def __str__ (self):
		return self.title

	def snippet(self):
 		return self.body[:17]+'...'
