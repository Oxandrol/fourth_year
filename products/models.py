from django.db import models


# Create your models here.
class Products(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.FloatField(default=0)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=256)
    created_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post.title} - {self.text}'
