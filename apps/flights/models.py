from django.db import models
from apps.settings.models import Currency
# Create your models here.
class Flights(models.Model):
    title = models.CharField(
        max_length=255
    )
    price = models.IntegerField(
    )
    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        related_name="flights_currency",
        verbose_name="Название валюты"
    )
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = "Авиабилет"
        verbose_name_plural = "Авиабилеты "
    