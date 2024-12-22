# Generated by Django 2.2.24 on 2024-12-22 19:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0006_complaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='who_liked',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]
