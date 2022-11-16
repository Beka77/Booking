from django.db import models
from apps.settings.models import Currency
# Create your models here.
class Cruises(models.Model):
    title = models.CharField(
        max_length=255
    )
    description = models.TextField()
    image = models.ImageField(
        upload_to= "cruises_image/"
    )
    price = models.IntegerField(
    )
    currency = models.ForeignKey(
        Currency,
        on_delete = models.CASCADE,
        related_name = "cruises_currency"
    )
    class Meta:
        verbose_name = "Круиз"
        verbose_name_plural = "Круизы"