from django.db import models
from apps.settings.models import Currency

# Create your models here.
class Hotels(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to= "cruises_image/")
    place = models.CharField(max_length=255)
    best = models.BooleanField(default=False)
    sale = models.IntegerField()
    price = models.IntegerField()
    airplane_prices = models.BigIntegerField()
    currency = models.ForeignKey(
        Currency,
        on_delete = models.CASCADE,
        related_name = "hotels_currency"
    )
    def __str__(self):
            return self.title
    
    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'     