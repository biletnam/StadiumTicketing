from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.core.urlresolvers import reverse
from core.utils.validators import validate_phonenumber


class UserProfile(AbstractUser):
    phone_number = models.CharField(validators=[validate_phonenumber], max_length=13,
                                    null=True, default='', help_text='eg +254712123456')
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    USER_PROFILE_REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    class Meta:
        ordering = ('-id', )

    def get_absolute_url(self):
        return reverse('userprofile:userprofile_detail', kwargs=({'slug': self.username, }))

    def get_update_url(self):
        return reverse('userprofile:userprofile_update', kwargs=({'slug': self.username, }))
