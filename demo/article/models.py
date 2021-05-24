from django.db import models

from django_geogebra.fields import GeoGebraCalculatorField


class Article(models.Model):
    graph = GeoGebraCalculatorField()
