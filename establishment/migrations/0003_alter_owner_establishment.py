# Generated by Django 4.0.1 on 2022-02-15 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('establishment', '0002_alter_establishment_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='establishment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_establishment', to='establishment.establishment'),
        ),
    ]
