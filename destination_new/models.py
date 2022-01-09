
from django.db import models

# Create your models here.
class categories(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name}"

class district(models.Model):
    d_name = models.CharField(max_length= 30)
    d_area = models.FloatField()
    def __str__(self):
        return f"{self.d_name}"

class destination(models.Model):
    title = models.CharField(max_length=40)
    iterinary = models.CharField(max_length=40)
    Cost = models.CharField(max_length=40)
    categories = models.ManyToManyField(categories)
    district = models.ForeignKey(district, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"{self.title}"
    
class new(models.Model):
    name = models.CharField(max_length=20)


class airport(models.Model):
    a_name = models.CharField(max_length=40)
    a_location = models.CharField(max_length=40 )
    a_image = models.ImageField(default='dragon_round.png')

    def __str__(self):
        return f"{self.a_name}"