from django.db import models

# Create your models here.
from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    authors = models.TextField()
    text = models.TextField()
    summary = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)