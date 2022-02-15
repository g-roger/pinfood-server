from django.db import models

from establishment.models import Establishment


class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    unit_price = models.FloatField()
    quantity = models.IntegerField(default=0)
    url_photo = models.TextField()
    date_available = models.DateTimeField(blank=True, null=True)
    date_limit = models.DateTimeField(blank=True, null=True)
    date_ended = models.DateTimeField(blank=True, null=True)

    establishment = models.OneToOneField(Establishment, on_delete=models.CASCADE, blank=True, null=True,
                                         related_name='products')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + ' - ' + self.establishment
