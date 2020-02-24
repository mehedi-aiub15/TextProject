from django.db import models

# Create your models here.
class Task(models.Model):
	id = models.AutoField(primary_key=True)
	Texts= models.TextField(blank=True,default='')

	def __str__(self):
		return self.Texts