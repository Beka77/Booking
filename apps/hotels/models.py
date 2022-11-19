from django.db import models
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

    def str(self):
        return self.title

    class Meta:
        verbose_name = "Отель"
        verbose_name_plural = "Отели"