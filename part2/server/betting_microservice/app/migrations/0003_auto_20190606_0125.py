# Generated by Django 2.2 on 2019-06-06 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190605_1730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bet',
            old_name='match',
            new_name='event',
        ),
    ]