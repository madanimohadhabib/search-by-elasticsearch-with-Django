from django.db import models



class Product(models.Model):
    title = models.CharField(max_length=150)
    category  =  models.CharField(max_length=150)
    description = models.TextField()
    prix = models.FloatField()
    def __str__(self):
        return self.title
