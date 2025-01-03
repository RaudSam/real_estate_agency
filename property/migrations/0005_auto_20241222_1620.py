# Generated by Django 2.2.24 on 2024-12-22 13:20

from django.db import migrations


def update_new_building_status(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(construction_year__gte=2015).update(new_building=True)
    Flat.objects.filter(construction_year__lt=2015).update(new_building=False)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(update_new_building_status)
    ]
