# Generated by Django 3.2.8 on 2021-11-05 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_service_datecreated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='address',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='name',
            new_name='service_name',
        ),
    ]
