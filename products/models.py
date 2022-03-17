from django.db import models


# Create your models here.
class Post(models.Model):
    title       = models.CharField(max_length=100) 
    description = models.TextField(max_length= 500, 
                blank=True, 
                null=True)
    category    = models.CharField(max_length= 200)
   # image       = models.ImageField(max_length=250, blank=True, null= True) 'pillow is not installed'
    price       = models.DecimalField(
                    decimal_places=2, 
                    max_digits=19)
    inStock=models.BooleanField(default=True)
    #stocked     = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        # ordering = ['-stocked']
        pass
