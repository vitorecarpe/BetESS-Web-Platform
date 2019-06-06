# Generated by Django 2.1.7 on 2019-06-06 12:04

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
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('oddV', models.FloatField()),
                ('oddE', models.FloatField()),
                ('oddD', models.FloatField()),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MatchesAndTeamsApp.Competition')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('simbolo', models.TextField()),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MatchesAndTeamsApp.Competition')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='equipaC',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipa_casa', to='MatchesAndTeamsApp.Team'),
        ),
        migrations.AddField(
            model_name='event',
            name='equipaV',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipa_visitante', to='MatchesAndTeamsApp.Team'),
        ),
    ]
