# Generated by Django 4.2.4 on 2023-12-25 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_homeinfomodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactbannermodel',
            name='image',
            field=models.ImageField(upload_to='contact_banners'),
        ),
    ]