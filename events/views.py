"""Contains all views of `events` app"""

from django.views.generic import ListView, DetailView, TemplateView
from .models import Event
from helpers.mixins import TitleMixin


class IndexView(TitleMixin, TemplateView):
    """Entry point view"""
    template_name = 'index.html'
    title = 'Index'

    def get_context_data(self, **kwargs):
        c = super(IndexView, self).get_context_data(**kwargs)
        c['events'] = Event.objects.all()
        return c


class EventListView(ListView):
    model = Event
    template_name = 'event/event_list.html'


class EventDetailView(DetailView):
    model = Event
    template_name = 'event/event_detail.html'
