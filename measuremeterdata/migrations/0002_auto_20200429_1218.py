# Generated by Django 3.0.5 on 2020-04-29 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measuremeterdata', '0001_squashed_0002_auto_20200429_0105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='country',
            name='comment',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='country',
            name='link_gov',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='link_worldometer',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='measure',
            name='comment',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='country',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='measuremeterdata.Continent'),
        ),
    ]
