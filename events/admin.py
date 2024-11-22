# admin.py
from django.contrib import admin
from .models import Event, EventRegistration

class EventRegistrationInline(admin.TabularInline):
    model = EventRegistration
    extra = 0

class EventAdmin(admin.ModelAdmin):
    inlines = [EventRegistrationInline]
    list_display = ('name', 'date', 'registration_count')

    def registration_count(self, obj):
        return EventRegistration.objects.filter(event=obj).count()

admin.site.register(Event, EventAdmin)
admin.site.register(EventRegistration)
