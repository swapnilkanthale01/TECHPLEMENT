from django.db import models

# Create your models here.
class Quote(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return f"{self.text} - {self.author}"
