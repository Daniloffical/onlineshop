from django.db import models

# Create your models here.
class Film(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField() 
    img = models.ImageField(upload_to="image/%Y/%m/%d")
    

    def __str__(self):
        return self.name