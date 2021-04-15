import urllib.parse

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from app.settings import BUS_STATION_CSV as BS
import csv


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    stations = []
    with open(BS) as bs:
        reader = csv.DictReader(bs)
        for row in reader:
            dict_bus = {'Name': row['Name'], 'Street': row['Street'], 'District': row['District']}
            stations.append(dict_bus)

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(stations, 10)
    page = paginator.get_page(page_number)

    if page.has_next():
        next_page_url = reverse('bus_stations') + "?" + urllib.parse.urlencode({'page': page.next_page_number()})
    else:
        next_page_url = None
    if page.has_previous():
        prev_page = reverse('bus_stations') + "?" + urllib.parse.urlencode({'page': page.previous_page_number()})
    else:
        prev_page = None

    return render(request, 'index.html', context={
        'bus_stations': page,
        'current_page': page_number,
        'prev_page_url': prev_page,
        'next_page_url': next_page_url,
    })
