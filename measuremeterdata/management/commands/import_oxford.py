from django.core.management.base import BaseCommand, CommandError
from measuremeterdata.models.models import Country, MeasureCategory, MeasureType, Measure, Continent, CasesDeaths, OxfordMeasure, OxfordMeasureType
import os
import csv
import datetime
import requests
import pandas as pd
from datetime import date, datetime, timedelta
from decimal import *

class Command(BaseCommand):
    def handle(self, *args, **options):


        import_oxford(
            'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/c4_restrictions_on_gatherings.csv',
            1
        )

        import_oxford(
            'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/c1_school_closing.csv',
            2
        )

        import_oxford(
            'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/c2_workplace_closing.csv',
            3
        )

        import_oxford(
            'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/c3_cancel_public_events.csv',
            4
        )

        import_oxford(
            'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/c6_stay_at_home_requirements.csv',
            5
        )

        import_oxford(
            'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/c7_movementrestrictions.csv',
            6
        )

        import_oxford(
            'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/c8_internationaltravel.csv,',
            7
        )



        import_oxford(
            'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/h7_vaccination_policy.csv',
            8
        )

        import_oxford(
            'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/h6_facial_coverings.csv',
            9
        )

        import_oxford(
            'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/h2_testing_policy.csv',
            10
        )

def import_oxford(url, category):

      with requests.Session() as s:
        download = s.get(url)

        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')

        #Load countries
        cntries = []
        for cntry in Country.objects.all():
            if (cntry.iso_code):
                cntries.append(cntry.iso_code.lower())


        category = OxfordMeasureType.objects.get(pk=category)

        print(f"Load {category} into django")


        row_count = 0

        for row in cr:
            if row_count == 0:
                firstrow = row
            row_count += 1


            if len(row) > 1 and row[1].lower() in cntries:
                country=Country.objects.get(iso_code=row[1])

                col_num = 0
                last_level = 0
                measure = None
                for col in row:
                    if (col_num > 2):
                        if col != "" and int(col) != last_level:
                            start_date = datetime.strptime(firstrow[col_num], '%d%b%Y')
                            stop_date = start_date + timedelta(days=-1)
                            if measure:
                                measure.end = stop_date
                                measure.save()

                            level = int(col)

                            if level == 0:
                                comment = category.text_level0
                            elif level == 1:
                                comment = category.text_level1
                            elif level == 2:
                                comment = category.text_level2
                            elif level == 3:
                                comment = category.text_level3
                            elif level == 4:
                                comment = category.text_level4

                            try:
                                measure = OxfordMeasure.objects.get(country=country, type=category, start=start_date)
                                measure.level = level
                                measure.comment = comment
                                measure.last_level = last_level
                                measure.save()
                            except:
                                measure = OxfordMeasure(country=country, type=category, comment = comment, start=start_date, level=level, last_level = last_level)
                                measure.save()
                            last_level = int(col)

                    col_num += 1

