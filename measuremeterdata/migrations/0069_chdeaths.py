# Generated by Django 3.0.5 on 2020-12-01 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measuremeterdata', '0068_auto_20201121_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='CHDeaths',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('week', models.IntegerField(blank=True, null=True)),
                ('deaths', models.IntegerField(blank=True, null=True)),
                ('average_deaths', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True)),
                ('canton', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measuremeterdata.CHCanton')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
