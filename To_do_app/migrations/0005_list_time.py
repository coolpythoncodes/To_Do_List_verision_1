# Generated by Django 2.1.4 on 2018-12-08 10:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('To_do_app', '0004_auto_20181208_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='time',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]