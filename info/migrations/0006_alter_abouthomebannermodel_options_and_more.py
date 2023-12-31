# Generated by Django 4.2.4 on 2023-10-22 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_delete_aboutclientmodel_delete_abouttestimonialmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='abouthomebannermodel',
            options={'verbose_name': 'about banner', 'verbose_name_plural': 'about banners'},
        ),
        migrations.AlterModelOptions(
            name='aboutinfomodel',
            options={'verbose_name': 'about info', 'verbose_name_plural': 'about info'},
        ),
        migrations.RenameField(
            model_name='aboutstatisticsmodel',
            old_name='stat1',
            new_name='stat',
        ),
        migrations.RenameField(
            model_name='aboutstatisticsmodel',
            old_name='stat_title1',
            new_name='stat_title',
        ),
        migrations.RemoveField(
            model_name='aboutstatisticsmodel',
            name='stat2',
        ),
        migrations.RemoveField(
            model_name='aboutstatisticsmodel',
            name='stat3',
        ),
        migrations.RemoveField(
            model_name='aboutstatisticsmodel',
            name='stat4',
        ),
        migrations.RemoveField(
            model_name='aboutstatisticsmodel',
            name='stat_title2',
        ),
        migrations.RemoveField(
            model_name='aboutstatisticsmodel',
            name='stat_title3',
        ),
        migrations.RemoveField(
            model_name='aboutstatisticsmodel',
            name='stat_title4',
        ),
    ]
