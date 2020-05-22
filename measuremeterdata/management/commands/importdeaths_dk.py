from django.core.management.base import BaseCommand, CommandError
from measuremeterdata.models import Country, MeasureCategory, MeasureType, Measure, Continent, CasesDeaths
import os
import csv
import datetime
from datetime import timedelta
import requests
import pandas as pd

class Command(BaseCommand):

    def handle(self, *args, **options):

        country = Country.objects.get(pk=8)
        with open('/app/measuremeterdata/datasources/denmark.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

            rowcount = 0
            savedate = datetime.date(2020,1,1)
            for row in spamreader:
                rowcount += 1
                if (rowcount == 5):
                    cellcount = 0
                    for cell in row:
                        cellcount += 1
                        if (cellcount > 2):
                            try:
                                cd_existing = CasesDeaths.objects.get(country=country, date=savedate)
                                print(cd_existing)
                                cd_existing.deathstotal = cell
                                cd_existing.save()
                            except CasesDeaths.DoesNotExist:
                                cd = CasesDeaths(country=country, deathstotal=cell, date=savedate)
                                cd.save()

                            savedate += timedelta(days=1)

                            print(savedate)
                            print(cell)
                            print("....")


