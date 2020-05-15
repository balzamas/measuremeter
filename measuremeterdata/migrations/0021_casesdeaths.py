# Generated by Django 3.0.5 on 2020-05-15 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measuremeterdata', '0020_auto_20200513_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='CasesDeaths',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('cases', models.IntegerField(default=0)),
                ('deaths', models.IntegerField(default=0)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measuremeterdata.Country')),
            ],
        ),
    ]