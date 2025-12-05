from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class BLog(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    content = RichTextField()
    disception = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)  
     

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    posts = models.ForeignKey(BLog, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name