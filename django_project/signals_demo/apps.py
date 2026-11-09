from django.apps import AppConfig


class SignalsDemoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signals_demo'


    #importing module registers
    def ready(self):
        from . import signals