from collections import Counter
from django.http import HttpResponse

from django.shortcuts import render


counter_show = Counter()
counter_click = Counter()


def index(request):
    if request.GET.get('from-landing') == 'original':
        counter_click['original'] += 1
    elif request.GET.get('from-landing') == 'test':
        counter_click['test'] += 1
    return render(request, 'index.html')


def landing(request):
    if request.GET.get('ab-test-arg') == 'original':
        counter_show['original'] += 1
        return render(request, 'landing.html')
    elif request.GET.get('ab-test-arg') == 'test':
        counter_show['test'] += 1
        return render(request, 'landing_alternate.html')


def stats(request):
    if counter_show['original'] != 0 and counter_show['test'] != 0:
        origin = counter_click['original']/counter_show['original']
        test = counter_click['test']/counter_show['test']
        return render(request, 'stats.html', context={
            'test_conversion': origin,
            'original_conversion': test,
        })
    else:
        msg = 'Невозможно получить соотношение, так как количество переходов равно 0'
        return HttpResponse(msg)
