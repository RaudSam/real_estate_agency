from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    new_building = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True
    )
    description = models.TextField('Текст объявления', blank=True)
    price = models.PositiveIntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True
    )
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное'
    )
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4'
    )
    floor = models.CharField(
        'Этаж',
        max_length=20,
        help_text='Первый этаж, последний этаж, пятый этаж'
    )

    rooms_number = models.PositiveIntegerField(
        'Количество комнат в квартире',
        db_index=True
    )
    living_area = models.PositiveIntegerField(
        'Количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True
    )

    has_balcony = models.BooleanField('Наличие балкона',
                                      null=True, db_index=True)
    active = models.BooleanField('Активно ли объявление', db_index=True)
    construction_year = models.PositiveIntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True
    )

    who_liked = models.ManyToManyField(User,
                                       verbose_name="Кто лайкнул",
                                       blank=True,
                                       related_name='liked_flats')

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=True,
                             blank=True,
                             verbose_name="Кто жаловался",
                             related_name='complaints')
    flat = models.ForeignKey(Flat,
                             on_delete=models.CASCADE,
                             null=True,
                             blank=True,
                             verbose_name="Квартира, на которую подали жалобу",
                             related_name='complaints')
    decription = models.TextField(null=True,
                                  blank=True,
                                  verbose_name="Текст жалобы")


class Owner(models.Model):
    name = models.CharField('ФИО владельца',
                            max_length=200,
                            db_index=True)
    phonenumber = models.CharField('Номер владельца',
                                   max_length=20)
    pure_phonenumber = PhoneNumberField('Нормализованный номер владельца',
                                        blank=True, null=True)
    flats = models.ManyToManyField(Flat,
                                   verbose_name='Квартиры в собственности',
                                   related_name='owners',
                                   db_index=True)

    def __str__(self):
        return self.name
