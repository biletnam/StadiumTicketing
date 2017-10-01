from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.core.urlresolvers import reverse
from core.utils.validators import validate_phonenumber


VALID_IMAGE_MIMES = ['image/jpeg', 'image/png']


class UserProfile(AbstractUser):
    phone_number = models.CharField(validators=[validate_phonenumber], max_length=13, null=True, blank=True, unique=True, help_text='eg +254712123456')
    profile_picture = models.FileField(upload_to='profile_pictures', null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    class Meta:
        ordering = ('-id', )

    def get_absolute_url(self):
        return reverse('accounts-app:user-profile-view', kwargs=({'slug': self.username, }))

    def get_update_url(self):
        return reverse('accounts-app:update-profile-view', kwargs=({'slug': self.username, }))
