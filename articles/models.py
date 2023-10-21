from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title =models.CharField(max_length=100)
    body =models.TextField()
    slug =models.SlugField()
    date =models.DateTimeField(auto_now_add=True)
    thumb =models.ImageField(upload_to='images/',default='default.jpg',blank=True)
    audio = models.FileField(upload_to='audio/', blank=True)
    video = models.FileField(upload_to='video/', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
  
    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:50]+'...'
    
    
    

