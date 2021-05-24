# Django Geogebra

This package provides Geogebra integration for Django.

## Installation

Will be available soon...

## Usage

```python
from django.db import models
from django_geogebra.fields import GeoGebraCalculatorField


class Article(models.Model):
    ...
    graph = GeoGebraCalculatorField()
```