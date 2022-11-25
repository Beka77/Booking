from django.db import models
from apps.settings.models import Currency

# Create your models here.
class Car(models.Model):
    title = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='cars/')
    description = models.TextField()
    price = models.IntegerField()
    currency = models.ForeignKey(
        Currency,
        on_delete = models.CASCADE,
        related_name = "cars_currency"
    )
     
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'