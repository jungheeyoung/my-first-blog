from django import forms
from django.db import models
# Create your models here.
from django.utils import timezone

def check_length(title):
	if len(title)<10:
		raise forms.ValidationError('10글자 이상 !!')

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length = 200, validators=[check_length])
	text = models.TextField()
	created_date = models.DateTimeField(
		default = timezone.now)
	published_date = models.DateTimeField(
		blank = True, null = True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title