from django.contrib import admin

from .forms import AdminCreateEventForm
from .models import Event, EventBook


class AdminEvent(admin.ModelAdmin):
    list_display = ('name', 'event_date', 'timestamp', 'is_payable', 'is_active')
    list_filter = ('timestamp', 'is_active', 'is_payable', 'event_date')
    search_fields = ('name', )
    prepopulated_fields = {
        'slug': ('name', )
    }
    form = AdminCreateEventForm

class AdminEventBook(admin.ModelAdmin):
    list_display = ('event', 'user', 'timestamp')
    list_filter = ('timestamp', )


admin.site.register(Event, AdminEvent)
admin.site.register(EventBook, AdminEventBook)