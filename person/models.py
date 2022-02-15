from django.db import models


# from django.contrib.gis.db.models import PointField


class Address(models.Model):
    name = models.CharField(max_length=120)
    lat = models.DecimalField(decimal_places=4, max_digits=12, blank=True, null=True)
    lon = models.DecimalField(decimal_places=4, max_digits=13, blank=True, null=True)
    zip_code = models.IntegerField()
    number = models.CharField(max_length=120, default='empty')
    street = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    country = models.CharField(max_length=120)

    # location = PointField(geography=True, default=Point(0.0, 0.0))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + ' - ' + str(self.zip_code) + ' - ' + self.number + ' - ' + self.state


class Person(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    is_email_confirmed = models.BooleanField(default=False)
    url_photo = models.CharField(max_length=255)
    is_owner = models.BooleanField(default=False)

    address = models.OneToOneField(Address, on_delete=models.CASCADE, blank=True, null=True
                                   , related_name='person_address')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    @property
    def token(self):
        return None

    def __str__(self):
        if self.is_owner:
            return '****' + self.first_name + ' ' + self.last_name + ' - ' + self.email
        return self.first_name + ' ' + self.last_name
