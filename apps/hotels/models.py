from django.db import models
# Create your models here.
class Hotels(models.Model):
    title = models.CharField(
        max_length=255
    )
    description = models.TextField()
    image = models.ImageField(
        upload_to= "cruises_image/"
    )
    price = models.IntegerField(
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Отель"
        verbose_name_plural = "Отели"