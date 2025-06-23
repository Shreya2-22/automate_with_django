from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'greet the user'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name of the user to greet')

    def handle(self, *args, **kwargs):
        # we write the logic
        name = kwargs['name']
        greeting = f'Hi {name}, Good Morning!'
        self.stdout.write(self.style.SUCCESS(greeting))
        