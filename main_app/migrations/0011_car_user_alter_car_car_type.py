# Generated by Django 4.0.4 on 2022-04-21 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0010_car_location_alter_car_car_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='car_type',
            field=models.CharField(choices=[('Minivans', 'Minivans'), ('Trucks', 'Trucks'), ('Crossovers', 'Crossovers'), ('Hatchback', 'Hatchback'), ('SUVs', 'SUVs'), ('Convertible', 'Convertible'), ('Van', 'Van'), ('Coupes', 'Coupes'), ('Sedan', 'Sedan')], max_length=100),
        ),
    ]
