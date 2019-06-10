# Generated by Django 2.2 on 2019-06-09 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190606_0126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='competition',
        ),
        migrations.CreateModel(
            name='TeamCompetition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Competition')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Team')),
            ],
        ),
    ]
