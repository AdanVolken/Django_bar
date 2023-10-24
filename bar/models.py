from django.db import models

# Create your models here.
class Bebida(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    alcoholic = models.BooleanField()
    description = models.TextField()
    image = models.ImageField(upload_to='bar/image')