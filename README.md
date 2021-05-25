# Django GeoGebra

This package provides [GeoGebra](https://www.geogebra.org/) integration for Django.

## Installation

Add an app to `INSTALLED_APPS`:

```python
# settings.py
INSTALLED_APPS = [
    ...,
    'django_geogebra',
]
```

## Usage

```python
from django.db import models
from django_geogebra.fields import GeoGebraCalculatorField


class Article(models.Model):
    ...
    graph = GeoGebraCalculatorField()
```
