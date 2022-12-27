import django_tables2 as tables
from django_tables2 import TemplateColumn
from .models import Event

class EventTable(tables.Table):
    class Meta:
        model = Event
        # add class="paleblue" to <table> tag
        attrs = {'class': 'table table-sm'}
        per_page = 30
        exclude = ('id', )

    #edit = TemplateColumn(template_name='pages/tables/training_update_column.html')