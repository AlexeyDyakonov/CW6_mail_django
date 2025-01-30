from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main"

    def ready(self):
        import time

        from .scheduler import start
        time.sleep(3)
        start()
