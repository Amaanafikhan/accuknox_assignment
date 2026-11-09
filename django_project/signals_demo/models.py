from django.db import models

# Create your models here.
class Q1Record(models.Model):
    """Used by Q1: its post_save receiver sleeps for 5 seconds."""
    name = models.CharField(max_length=100)


class Q2Record(models.Model):
    """Used by Q2: its post_save receiver prints the thread ID."""
    name = models.CharField(max_length=100)


class Q3Record(models.Model):
    """Used by Q3: its post_save receiver writes a row to AuditLog."""
    name = models.CharField(max_length=100)


class AuditLog(models.Model):
    """Row written by the Q3 receiver, so we can check whether it was rolled back."""
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
