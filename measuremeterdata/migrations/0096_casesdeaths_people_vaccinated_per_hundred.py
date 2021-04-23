# Generated by Django 3.0.5 on 2021-03-12 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measuremeterdata', '0095_casesdeaths_death_to_cases'),
    ]

    operations = [
        migrations.AddField(
            model_name='casesdeaths',
            name='people_vaccinated_per_hundred',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True),
        ),
    ]