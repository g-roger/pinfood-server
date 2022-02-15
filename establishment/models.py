from django.db import models

from person.models import Address, Person


class Establishment(models.Model):
    name = models.CharField(max_length=120)
    registration_code = models.CharField(max_length=120)
    url_photo = models.CharField(max_length=255, null=True)
    open_weekend_at = models.TimeField(default='09:00:00', null=True)
    close_weekend_at = models.TimeField(default='23:00:00', null=True)
    open_week_at = models.TimeField(default='09:00:00', null=True)
    close_week_at = models.TimeField(default='18:00:00', null=True)
    phone_number = models.CharField(max_length=255, null=True)
    is_open = models.BooleanField(default=False)

    address = models.OneToOneField(Address, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='establishment_address')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + ' - ' + self.registration_code


class Owner(models.Model):
    cod_cmvs = models.CharField(max_length=255, null=True)
    cod_avcb = models.CharField(max_length=255, null=True)

    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='owner')
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE, related_name='owner_establishment')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.cod_cmvs + ' - ' + str(self.person) + ' - ' + str(self.establishment)
