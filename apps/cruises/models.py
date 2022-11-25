from django.db import models
from apps.settings.models import Currency
# Create your models here.
class Cruises(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    poster = models.ImageField('cruiese/')
    place = models.CharField(max_length=100)
    rate = models.CharField(max_length=100)
    price = models.BigIntegerField()
    currency = models.ForeignKey(
        Currency,
        on_delete = models.CASCADE,
        related_name = "cruises_currency"
    )
     
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Круиз'
        verbose_name_plural = 'Круизы'