from django.apps import AppConfig


class AppAdminConfig(AppConfig):
    name = 'app_admin'

    def ready(self):
        from . import signals