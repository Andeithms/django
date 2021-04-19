from django.shortcuts import render
import csv
from .settings import INFl


def inflation_view(request):
    template_name = 'inflation.html'
    # чтение csv-файла и заполнение контекста
    context = {}
    list_for_context = []
    with open(INFl, encoding='utf-8') as f:
        file_reader = csv.reader(f)
        for i, string in enumerate(file_reader):
            for elem in string:
                new_list = elem.split(';')

            if i == 0:  # запись месяцев
                list_for_context.append(new_list)
            else:
                interim_list = []
                for x in new_list[1:]:  # чтобы год не стал float
                    try:  # чтобы избежать ошибки при пустых ячейках
                        interim_list.append(float(x))
                    except ValueError:
                        interim_list.append('-')
                interim_list.insert(0, new_list[0])
                list_for_context.append(interim_list)

    context['name'] = list_for_context

    return render(request, template_name,
                  context)
