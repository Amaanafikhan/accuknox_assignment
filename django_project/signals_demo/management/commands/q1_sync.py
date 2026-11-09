import time

from django.core.management.base import BaseCommand

from signals_demo.models import Q1Record


class Command(BaseCommand):
    help = "Q1: show that Django signals run synchronously"

    def handle(self, *args, **options):
        self.stdout.write("[caller] calling save()...")

        start = time.time()
        Q1Record.objects.create(name="q1 test")
        elapsed = time.time() - start

        self.stdout.write(f"[caller] save() returned after {elapsed:.2f} seconds")

        if elapsed >= 5:
            self.stdout.write(self.style.SUCCESS(
                "Result: the caller waited for the receiver -> signals are SYNCHRONOUS"
            ))
        else:
            self.stdout.write(self.style.ERROR(
                "Result: save() returned early -> signals would be asynchronous"
            ))