from django.apps import AppConfig


class HtConfig(AppConfig):
    name = 'ht_web_service.apps.ht'

    def ready(self):
        from .import signals
