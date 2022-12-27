import django_filters as df
from .models import Event


class EventListFilter(df.FilterSet):
    class Meta:
        model = Event
        exclude = ('id', )

