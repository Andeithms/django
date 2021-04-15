from django.urls import path, register_converter
from app.views import *
from .converter import DtConverter

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам
register_converter(DtConverter, 'dtc')

urlpatterns = [
    path('', file_list, name='file_list'),
    path('<dtc:dt>/', file_list, name='file_list'),
    path('file_content/<name>/', file_content, name='file_content'),
]
