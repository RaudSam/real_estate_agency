# Generated by Django 2.2.24 on 2024-12-23 16:11

from django.db import migrations


def add_flat_in_owner(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    owners = Owner.objects.iterator()
    for owner in owners:
        flats = Flat.objects.filter(owner=owner.name)
        owner.flats.set(flats)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20241223_1749'),
    ]

    operations = [
        migrations.RunPython(add_flat_in_owner)
    ]
