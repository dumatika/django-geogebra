from django.conf import settings
from django.forms.widgets import TextInput


class GeogebraCalculatorFieldWidget(TextInput):
    input_type = 'geogebra'
    template_name = 'sandbox/geogebra-field-widget.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['geogebra'] = settings.DJANGO_GEOGEBRA
        return context
