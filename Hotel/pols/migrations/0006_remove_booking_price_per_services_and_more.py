# Generated by Django 5.0.6 on 2024-06-08 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pols', '0005_alter_hotel_stars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='price_per_services',
        ),
        migrations.AlterField(
            model_name='booking',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
