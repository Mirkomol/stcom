from django.apps import AppConfig


class StusersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stusers'



    def ready(self):
        import stusers.signals