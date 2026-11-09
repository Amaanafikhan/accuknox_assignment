from django.core.management.base import BaseCommand

from signals_demo.rectangle import Rectangle


class Command(BaseCommand):
    help = "Iterate over a Rectangle instance"

    def handle(self, *args, **options):
        rect = Rectangle(10, 5)
        for item in rect:
            self.stdout.write(str(item))
            