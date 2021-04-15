from datetime import datetime
import os
from django.shortcuts import render


def file_list(request, dt=None):
    template_name = 'index.html'
    servers_list = []
    files = os.listdir(r'D:\django\SecondProject\file_server\files')

    for i in files:
        server = os.stat(rf'D:\django\SecondProject\file_server\files\{i}')
        modified = datetime.fromtimestamp(server.st_mtime).strftime('%Y-%m-%d %H:%M')  # время последнего изменения
        create = datetime.fromtimestamp(server.st_ctime).strftime('%Y-%m-%d %H:%M')  # дата создания
        servers = {'name': i, 'ctime': create, 'mtime': modified}
        servers_list.append(servers)

    context = {'files': servers_list, 'date': dt}
    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    files = os.listdir(r'D:\django\SecondProject\file_server\files')
    if name in files:
        server = rf'D:\django\SecondProject\file_server\files\{name}'
        with open(server, encoding='utf-8') as f:
            text = f.readlines()
            context = ('\n'.join(i.strip() for i in text))
            return render(
                request,
                'file_content.html',
                context={'file_name': name, 'file_content': context}
            )


