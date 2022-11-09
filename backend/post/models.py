from django.db import models

# Create your models here.
class Post(models.Model):
    userPost = models.CharField(max_length=100)
    content = models.CharField(max_length=200000)
    
    def __str__(self):
        return f'{self.userPost} ,{self.content}'