# Generated by Django 4.0.1 on 2022-02-11 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0005_remove_person_addresses_person_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_cmvs', models.CharField(max_length=255, null=True)),
                ('cod_avcb', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('establishment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='establishment', to='person.person')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='person.person')),
            ],
        ),
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('registration_code', models.CharField(max_length=120)),
                ('url_photo', models.CharField(max_length=255, null=True)),
                ('open_weekend_at', models.TimeField(default='09:00:00', null=True)),
                ('close_weekend_at', models.TimeField(default='23:00:00', null=True)),
                ('open_week_at', models.TimeField(default='09:00:00', null=True)),
                ('close_week_at', models.TimeField(default='18:00:00', null=True)),
                ('phone_number', models.CharField(max_length=255, null=True)),
                ('is_open', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='person.address')),
            ],
        ),
    ]