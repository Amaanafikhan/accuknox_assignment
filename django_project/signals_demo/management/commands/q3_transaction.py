from django.core.management.base import BaseCommand
from django.db import transaction

from signals_demo.models import AuditLog, Q3Record


class Command(BaseCommand):
    help = "Q3: show that Django signals run in the same database transaction as the caller"

    def handle(self, *args, **options):
        # start clean so the counts are easy to read
        Q3Record.objects.all().delete()
        AuditLog.objects.all().delete()

        self.stdout.write("[caller] opening transaction.atomic()")
        try:
            with transaction.atomic():
                Q3Record.objects.create(name="q3 test")
                self.stdout.write(
                    f"[caller] inside the transaction: "
                    f"Q3Record={Q3Record.objects.count()}, AuditLog={AuditLog.objects.count()}"
                )
                raise RuntimeError("forcing a rollback")
        except RuntimeError:
            self.stdout.write("[caller] error raised -> transaction rolled back")

        q3_count = Q3Record.objects.count()
        log_count = AuditLog.objects.count()
        self.stdout.write(f"[caller] after rollback: Q3Record={q3_count}, AuditLog={log_count}")

        if q3_count == 0 and log_count == 0:
            self.stdout.write(self.style.SUCCESS(
                "Result: the receiver's AuditLog row was rolled back too -> "
                "signals run in the SAME TRANSACTION as the caller"
            ))
        else:
            self.stdout.write(self.style.ERROR(
                "Result: the AuditLog row survived -> receiver was outside the transaction"
            ))