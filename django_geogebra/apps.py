from django.apps import AppConfig
from django.conf import settings

from django_geogebra.settings import DEFAULTS
from .settings import SETTING_NAME


class SandboxConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_geogebra'

    def ready(self):
        config = DEFAULTS
        if hasattr(settings, SETTING_NAME):
            config = {**config, **settings.DJANGO_GEOGEBRA}

        setattr(settings, SETTING_NAME, config)
