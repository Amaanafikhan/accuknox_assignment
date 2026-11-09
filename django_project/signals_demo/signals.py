import threading
import time

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import AuditLog, Q1Record, Q2Record, Q3Record


# If they are synchronous,the caller waits 5s.
@receiver(post_save, sender=Q1Record)
def q1_slow_receiver(sender, instance, created, **kwargs):
    print("[receiver] started, sleeping for 5 seconds...")
    time.sleep(5)
    print("[receiver] finished")


# Q2 - print the thread this receiver runs on, to compare with the caller.
@receiver(post_save, sender=Q2Record)
def q2_thread_receiver(sender, instance, created, **kwargs):
    t = threading.current_thread()
    print(f"[receiver] thread id = {threading.get_ident()}, name = {t.name}")


# Q3 - write to another table. If the caller's transaction rolls back
# and this row disappears too, the receiver was inside the same transaction.
@receiver(post_save, sender=Q3Record)
def q3_audit_receiver(sender, instance, created, **kwargs):
    in_atomic = transaction.get_connection().in_atomic_block
    print(f"[receiver] inside atomic block? {in_atomic}")
    AuditLog.objects.create(message=f"Q3Record '{instance.name}' saved")