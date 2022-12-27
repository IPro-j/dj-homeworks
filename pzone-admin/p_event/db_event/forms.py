from django import forms
from .models import Event
from crispy_forms.helper import FormHelper


class EventListFormHelper(FormHelper):
    model = Event
    form_tag = False