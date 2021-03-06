from django.core.management.base import BaseCommand, CommandError
from measuremeterdata.models.models import Country, MeasureCategory, Continent, CasesDeaths
import os
import csv
import datetime
from datetime import timedelta
import requests
import pandas as pd

def CalcCaesesPer100k(cases, population):
    casespm = int(cases) *100000 / (int(population))
    return casespm

class Command(BaseCommand):

    def handle(self, *args, **options):

        country = Country.objects.get(pk=23)

        url = country.source_death

        myfile = requests.get(url)

        print("Read excel")
        read_file = pd.read_excel(myfile.content, sheet_name = "Tabell 1")
        print("Convert and write:")
        read_file.to_csv('/tmp/death_se.csv', index=None, header=True)



        workpath = os.path.dirname(os.path.abspath(__file__))  # Returns the Path your .py file is in

        print("Load data into django")
        # Should move to datasources directory
        with open('/tmp/death_se.csv', newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

                rowcount = 0
                savedate = datetime.date(2020,1,1)
                for row in spamreader:
                    rowcount += 1
                    if (rowcount > 7 and rowcount < 374 and int(float(row[6]))>0):
                        print(savedate)
                        print(row[6])
                        print("-----")

                        try:
                            cd_existing = CasesDeaths.objects.get(country=country, date=savedate)
                            print(cd_existing)
                            cd_existing.deathstotal = int(float(row[6]))
                            cd_existing.deaths_total_per100k = CalcCaesesPer100k(int(float(row[6])), country.population)
                            cd_existing.save()
                        except CasesDeaths.DoesNotExist:
                            cd = CasesDeaths(country=country, deathstotal=int(float(row[6])), date=savedate, deaths_total_per100k = CalcCaesesPer100k(int(float(row[6])), country.population))
                            cd.save()


                        savedate += timedelta(days=1)








