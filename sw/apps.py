from django.apps import AppConfig


class SwConfig(AppConfig):
    name = 'sw'


    def ready(self):
        import sw.signals
        import sw.task