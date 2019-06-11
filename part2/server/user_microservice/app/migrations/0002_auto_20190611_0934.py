# Generated by Django 2.1.7 on 2019-06-11 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='coins',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]