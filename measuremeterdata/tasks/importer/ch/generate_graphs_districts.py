from pylab import figure, axes, pie, title, show
from django.core.management.base import BaseCommand, CommandError
from matplotlib import pyplot as plt
from measuremeterdata.models.models_ch import CHCanton, CHCases
import os
from datetime import datetime
from datetime import timedelta

def write_graph(canton, dates, data, suffix, ymax):
    plt.figure()

    fig, ax = plt.subplots()
    ax.plot(dates, data, color='#fed1a4')

    fig.patch.set_visible(False)
    ax.axis('off')

    plt.text(1, 0.5, r'an equation: $E=mc^2$', fontsize=15)

    # plt.xlabel("Age")
    # plt.ylabel("Total Population")
    # plt.title("Cases per 100k/past 7 days")
    plt.tight_layout()

    plt.fill_between(dates, data, color='#fed1a4')

    plt.ylim(0, ymax)

    figure = plt.gcf()

    figure.set_size_inches(2, 1)

    frame1 = plt.gca()
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)

    plt.savefig(f'measuremeter/static/images/graphs_ch/{canton.swisstopo_id}_{suffix}.png', dpi=100)
    plt.close()

def generate():
        path = os.getcwd()
        print(path)

        for canton in CHCanton.objects.filter(level=1):
            print(canton)

            cases7 = []
            cases14 = []
            dates = []

            for day in CHCases.objects.filter(canton=canton, date__gte=(datetime.today() - timedelta(days=62))).order_by('-date')[:61]:
               print(day.date)
               if (day.incidence_past14days):
                   cases14.append(float(day.incidence_past14days))
               else:
                   cases14.append(0)
               if (day.incidence_past7days):
                   cases7.append(float(day.incidence_past7days))
               else:
                   cases7.append(0)
               dates.append(day.date)

            write_graph(canton, dates, cases14, "14", None)
            write_graph(canton, dates, cases7, "7", None)
