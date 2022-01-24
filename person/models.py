from django.db import models
from django.contrib.gis.db.models import PointField


class Address(model.Model):
    name = model.CharField(max_length=120)
    lat = models.DecimalField(decimal_places=4, max_digits=12)
    lon = models.DecimalField(decimal_places=4, max_digits=13)
    zip_code = models.IntegerField()
    street = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    country = models.CharField(max_length=120)

    location = PointField(geography=True, default=Point(0.0, 0.0))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.name
