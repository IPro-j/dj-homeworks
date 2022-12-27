from django.contrib import admin
from .models import Object, Agent, ObjectPasport, ObjectState

admin.site.site_title = "<your_title>"
admin.site.site_header = "База данных. Протект Зон."
#admin.site.index_title = "<your_index_title>"

class AgentInline(admin.TabularInline):
    model = Agent
    extra = 10


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    #list_filter = ('number',)
    #inlines = [AgentInline, ]
    search_fields = ('number',)
    list_display = ('number', 'pasport_url', 'agent_url',)
    pass


@admin.register(ObjectPasport)
class ObjectPasportAdmin(admin.ModelAdmin):
    #list_filter = ('number',)
    search_fields = ('object__number',)
    readonly_fields = ['event1', 'event2', ]
    pass


@admin.register(ObjectState)
class ObjectPasportAdmin(admin.ModelAdmin):
    #list_filter = ('number',)
    search_fields = ('object__number',)
    pass


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    #list_filter = ('object__number',)
    search_fields = ('object__number',)
    autocomplete_fields = ['object', ]
    pass
