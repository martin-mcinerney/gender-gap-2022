from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=30)
    text = models.TextField(max_length=300)
    link = models.URLField(max_length=200, default="https://www.linkedin.com")
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.author
