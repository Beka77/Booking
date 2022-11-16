from django.db import models
from apps.settings.models import Currency
# Create your models here.
class Locations(models.Model):
    title = models.CharField(
        max_length=255
    )
    description = models.TextField()

    image = models.ImageField(
        upload_to= "locations_image/"
    )
    price = models.IntegerField(
    )
    currency = models.ForeignKey(
        Currency,
        on_delete = models.CASCADE,
        related_name = "locations_currency"
    )
     
    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"
 
