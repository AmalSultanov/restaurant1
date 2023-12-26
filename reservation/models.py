from django.db import models

from common_models import AbstractTimestampedModel


class ReservationBannerModel(AbstractTimestampedModel):
    image = models.ImageField(upload_to='reservation_banners')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'home banner'
        verbose_name_plural = 'home banners'


class ReservationModel(AbstractTimestampedModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    number_of_people = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'reservation'
        verbose_name_plural = 'reservations'
