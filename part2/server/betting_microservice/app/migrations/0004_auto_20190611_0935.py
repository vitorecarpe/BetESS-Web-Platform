# Generated by Django 2.1.7 on 2019-06-11 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190606_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='odd',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='bet',
            name='profit',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
