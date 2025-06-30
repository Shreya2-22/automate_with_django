from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv

#proposed command - python manage.py importdata <csv_file_path> model_name

class Command(BaseCommand):
    help = 'Import data from csv file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='Path to the CSV file containing data to import')
        parser.add_argument('model_name', type=str, help='Name of the model to import data into')

    def handle(self, *args, **kwargs):
        file_path = kwargs['csv_file_path']
        model_name = kwargs['model_name'].capitalize()  # Ensure the model name is capitalized
        #search for the model across all installed apps
        model = None
        for app_config in apps.get_app_configs():
            #try to search for the model
            try:
                model = apps.get_model(app_config.label, model_name)
                break # stop searching once the model is found
            except LookupError:
                continue #continue searching in the next app
            
        if not model:
            raise CommandError(f'Model "{model_name}" not found in any installed app.')
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)

        self.stdout.write(self.style.SUCCESS('Data imported from csv successfully!'))
