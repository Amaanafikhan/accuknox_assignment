import threading

from django.core.management.base import BaseCommand

from signals_demo.models import Q2Record


class Command(BaseCommand):
    help = "Q2: show that Django signals run in the same thread as the caller"

    def handle(self, *args, **options):
        t = threading.current_thread()
        self.stdout.write(f"[caller]   thread id = {threading.get_ident()}, name = {t.name}")

        Q2Record.objects.create(name="q2 test")

        self.stdout.write(self.style.SUCCESS(
            "Result: compare the two thread ids above - if they match, "
            "the receiver ran in the SAME THREAD as the caller"
        ))