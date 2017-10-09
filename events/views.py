"""Contains all views of `events` app"""

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import (CreateView, DetailView, ListView,
                                  TemplateView, UpdateView)
from .forms import EventBookCreateForm
from .models import Event, EventBook
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


class EventBookCreateView(CreateView):
    template_name = 'event/eventbook_create.html'
    form_class = EventBookCreateForm

    def get_form_kwargs(self):
        kw = super(EventBookCreateView, self).get_form_kwargs()
        if 'request' not in kw:  # add request to form
            kw.setdefault('request', self.request)

        if 'event' not in kw:  # add event to form
            event = Event.objects.get(slug=self.kwargs.get('slug'))
            kw.setdefault('event', event)
        return kw

    def get_context_data(self, **kwargs):
        c = super(EventBookCreateView, self).get_context_data(**kwargs)
        c['event'] = Event.objects.get(slug=self.kwargs.get('slug'))
        return c

    def get_success_url(self):
        messages.success(self.request, 'Your ticket has been created successfully, '
                                       'you may view it on your profile')
        return reverse('events:event_detail', kwargs={'slug': self.kwargs.get('slug')})


class EventBookUpdateView(UpdateView):
    form_class = EventBookCreateForm
    model = EventBook
    template_name = 'event/eventbook_create.html'
    pk_url_kwarg = 'ebid'

    def get_form_kwargs(self):
        kw = super(EventBookUpdateView, self).get_form_kwargs()
        if 'request' not in kw:  # add request to form
            kw.setdefault('request', self.request)

        if 'event' not in kw:  # add event to form
            pk = self.kwargs.get('ebid')
            event = EventBook.objects.get(pk=pk)
            event = event.event
            kw.setdefault('event', event)
        return kw

    def get_success_url(self):
        messages.success(self.request, 'Your ticket has been updated successfully, '
                                       'you may view it on your profile')
        return reverse('userprofile:userprofile_detail', kwargs={'slug': self.request.user.username})

    def get_context_data(self, **kwargs):
        c = super(EventBookUpdateView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('ebid')
        event = EventBook.objects.get(pk=pk)
        c['event'] = event.event
        return c
