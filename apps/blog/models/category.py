from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.title
