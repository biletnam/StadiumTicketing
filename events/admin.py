from django.contrib import admin

from .models import Event


class AdminEvent(admin.ModelAdmin):
    list_display = ('name', 'event_date', 'timestamp', 'is_active')
    prepopulated_fields = {
        'slug': ('name', )
    }


admin.site.register(Event, AdminEvent)