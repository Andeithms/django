import json

from django.core.management.base import BaseCommand
from school.models import Student, Teacher
from website.settings import FILE_PATH


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(FILE_PATH, 'r',  encoding='utf8') as f:
            data = json.load(f)
        for person in data:
            if person['model'] == 'school.student':
                student = Student.objects.create(id=person['pk'],
                                                 name=person['fields']['name'],
                                                 group=person['fields']['group'])
                teacher_id = person['fields']['teacher']
                student.teacher.add(Teacher.objects.get(id=teacher_id))
                student.save()
            elif person['model'] == 'school.teacher':
                teacher = Teacher.objects.create(id=person['pk'],
                                                 name=person['fields']['name'],
                                                 subject=person['fields']['subject'])
                teacher.save()
