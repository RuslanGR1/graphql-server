from django.db import models

class Comment(models.Model):
    text = models.TextField()

    def __str__(self) -> str:
        return self.text
