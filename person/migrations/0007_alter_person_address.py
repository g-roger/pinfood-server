# Generated by Django 4.0.1 on 2022-02-14 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0006_address_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person_address', to='person.address'),
        ),
    ]
