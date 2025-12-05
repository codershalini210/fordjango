from django.db import models
class Movie(models.Model):
    title= models.CharField(max_length=200)
    director =models.CharField(max_length=200)
    release_year=models.IntegerField()
    rating = models.DecimalField(max_digits=3,decimal_places=1)
    synopsis = models.TextField()

    def __str__(self):
        return self.title
# Create your models here.
