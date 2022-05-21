from ast import arg
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


# Create your models here
class Category(models.Model):
    name = models.CharField(max_length=240)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
        #return reverse('post', args=(str(self.id)))

class Post(models.Model):
    title = models.CharField(max_length=240)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    summary = models.TextField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post_category = models.CharField(max_length = 255, default='')
    
    def __str__(self):
        return self.title + ' | ' + str(self.author )

    def get_absolute_url(self):
        return reverse('home')
        #return reverse('post', args=(str(self.id)))
