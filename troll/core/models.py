from django.db import models

# Create your models here.
class Comment(models.Model):
    """Model representing a comment"""
    text = models.TextField()

    def __str__(self):
        return self.text
