from django.db import models

from common_models import AbstractTimestampedModel


class AboutBannerModel(AbstractTimestampedModel):
    image = models.ImageField(upload_to='about_banners')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'about banner'
        verbose_name_plural = 'about banners'


class AboutInfoModel(AbstractTimestampedModel):
    image = models.ImageField(upload_to='about_info_images')
    upper_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'about info'
        verbose_name_plural = 'about info'


class AboutStatisticsPhotoModel(AbstractTimestampedModel):
    image = models.ImageField(upload_to='about_statistics')

    def __str__(self):
        return 'photo'

    class Meta:
        verbose_name = 'statistics photo'
        verbose_name_plural = 'statistics photos'


class AboutStatisticsModel(AbstractTimestampedModel):
    stat_number = models.PositiveIntegerField()
    stat_title = models.CharField(max_length=100)

    def __str__(self):
        return self.stat_title

    class Meta:
        verbose_name = 'statistics'
        verbose_name_plural = 'statistics'


class StaffBannerModel(AbstractTimestampedModel):
    image = models.ImageField(upload_to='staff_banners')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'staff banner'
        verbose_name_plural = 'staff banners'


class StaffModel(AbstractTimestampedModel):
    image = models.ImageField(upload_to='staff_images')
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'staff'
        verbose_name_plural = 'staff'
