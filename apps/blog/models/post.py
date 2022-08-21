from django.db import models
from django.contrib.auth.models import User

from .category import Category

class Post(models.Model):

    title = models.CharField(max_length=250)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
