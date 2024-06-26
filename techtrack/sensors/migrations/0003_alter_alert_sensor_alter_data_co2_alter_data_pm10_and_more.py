# Generated by Django 5.0.6 on 2024-06-01 16:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0002_alter_alert_timestamp_alter_data_timestamp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensors.sensor'),
        ),
        migrations.AlterField(
            model_name='data',
            name='co2',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='data',
            name='pm10',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='data',
            name='pm25',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='data',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensors.sensor'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='status',
            field=models.CharField(max_length=50),
        ),
    ]
