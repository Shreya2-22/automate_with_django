from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    help = 'it will insert data into the database'

    def handle(self, *args, **kwargs):
        dataset = [
            {'roll_number':1002, 'name':'Sraddha', 'age':20},
            {'roll_number':1003, 'name':'Siddharth', 'age':22 },
            {'roll_number':1004, 'name':'Safal', 'age':21},
            
        ]
        for data in dataset:
            roll_number = data['roll_number']
            if Student.objects.filter(roll_number=roll_number).exists():
                self.stdout.write(self.style.WARNING(f'Student with roll number {roll_number} already exists. Skipping insertion.'))
                continue
            # If the student does not exist, create a new record
            else:
                Student.objects.create(roll_number = data['roll_number'], name=data['name'], age=data['age'])
        self.stdout.write(self.style.SUCCESS('Data inserted successfully!'))