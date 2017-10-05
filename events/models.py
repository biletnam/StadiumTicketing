from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone


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

    def get_absolute_url(self):
        return reverse('events:event_detail', kwargs={'slug': self.slug, })

    def __str__(self):
        return self.name
