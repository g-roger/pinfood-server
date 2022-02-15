# Generated by Django 4.0.1 on 2022-02-01 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_alter_person_address_alter_person_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='lon',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=13, null=True),
        ),
    ]
