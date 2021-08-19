from django.apps import AppConfig


class AppUserConfig(AppConfig):
    name = 'app_user'

    def ready(self):
        from . import signals