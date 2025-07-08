import csv
from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from datetime import datetime

#proposed command = python manage.py exportdata model_name

class Command(BaseCommand):
    help='Export data from the database to a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='The name of the model to export data from')

    def handle(self, *args, **kwargs):
        model_name = kwargs['model_name'].capitalize()

        #search through all installed apps for the model
        model = None
        for app in apps.get_app_configs():
            try:
                model = app.get_model(model_name)
                break
            except LookupError:
                continue
        if model is None:
            raise CommandError(f'Model "{model_name}" not found in any installed app.')
        # Get the model's fields
        data = model.objects.all()

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'{model_name}_{timestamp}.csv'
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Write the header
            writer.writerow([field.name for field in model._meta.fields])
            # Write the data
            for obj in data:
                writer.writerow([getattr(obj, field.name) for field in model._meta.fields])
        self.stdout.write(self.style.SUCCESS(f'Data exported successfully to {filename}'))
        return filename
