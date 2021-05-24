from django.forms.widgets import TextInput


class GeogebraCalculatorFieldWidget(TextInput):
    input_type = 'geogebra'
    template_name = 'sandbox/geogebra-field-widget.html'
