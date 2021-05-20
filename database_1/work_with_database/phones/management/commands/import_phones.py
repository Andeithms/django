import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone
from main.settings import FILE_PATH


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(FILE_PATH) as f:
            phone_reader = csv.reader(f, delimiter=';')
            next(phone_reader)
            for line in phone_reader:
                phone_db = Phone(id=line[0],
                                 name=line[1],
                                 image=line[2],
                                 price=line[3],
                                 release_date=line[4],
                                 lte_exists=line[5],
                                 slug=slugify(line[1], allow_unicode=True))
                phone_db.save()

