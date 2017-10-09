from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from accounts.models import UserProfile


class Event(models.Model):

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100,
                            null=True, blank=True,
                            help_text="Leave this field blank")
    description = models.TextField()
    main_image = models.ImageField(upload_to='events')
    event_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(default=timezone.now)
    is_payable = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                null=True, blank=True)

    @property
    def remaining_days(self):
        """
        count remaining days to the event date
        :return:
        """
        rem_days = self.event_date.date() - timezone.now().date()
        return rem_days.days

    @property
    def past_due(self):
        """
        Check if the event is past due to prevent users from
        booking for an event that has passed
        """
        return True if self.remaining_days < 0 else False

    def get_absolute_url(self):
        return reverse('events:event_detail', kwargs={'slug': self.slug, })

    def __str__(self):
        return self.name


class EventBook(models.Model):
    """
    A model that will record booking events
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile)
    tickets = models.IntegerField(default=1)
    amount = models.DecimalField(max_digits=10, decimal_places=2,
                                 max_length=10, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)

    @property
    def is_payable(self):
        """
        Check if the event being booked is payable
        """
        return True if self.event.is_payable else False

    class Meta:
        verbose_name_plural = 'Event Bookings'

    def __str__(self):
        return self.event.name
