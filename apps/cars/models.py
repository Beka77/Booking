from django.db import models
# Create your models here.
class Car(models.Model):
    title = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='cars/')
    description = models.TextField()
    volume = models.CharField(max_length=50)
    capacity = models.IntegerField()
    year = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'