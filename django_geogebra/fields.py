from django.db import models

from .widgets import GeogebraCalculatorFieldWidget


class GeoGebraCalculatorField(models.TextField):
    def formfield(self, **kwargs):
        kwargs['widget'] = GeogebraCalculatorFieldWidget
        return super().formfield(**kwargs)

# class Task(models.Model):
#     geogebra_task = GeoGebraCalculatorField()
