# Generated by Django 3.0.5 on 2020-08-04 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measuremeterdata', '0034_chmeasure_isregional'),
    ]

    operations = [
        migrations.AddField(
            model_name='chcanton',
            name='population',
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name='CHCases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('cases', models.IntegerField(default=0)),
                ('cases_past14days', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('canton', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measuremeterdata.CHCanton')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
