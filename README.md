# Django Geogebra

This package provides Geogebra integration for Django.

## Installation
Will be available soon...

## Usage
```python
# models.py
from django.db import models
from django_geogebra.fields import GeoGebraCalculatorField

class Article(models.Model):
    ...
    graph = GeoGebraCalculatorField()

# admin.py
from django.contrib import admin

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    ...
```