# Generated by Django 2.2 on 2019-06-06 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('simbolo', models.TextField()),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Competition')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('oddV', models.FloatField()),
                ('oddE', models.FloatField()),
                ('oddD', models.FloatField()),
                ('status', models.BooleanField(default=True)),
                ('result', models.TextField()),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Competition')),
                ('equipaC', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipa_casa', to='app.Team')),
                ('equipaF', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipa_fora', to='app.Team')),
            ],
        ),
    ]
