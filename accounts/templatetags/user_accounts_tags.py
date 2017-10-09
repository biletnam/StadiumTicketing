from django import http
from django import template
from django.conf import settings
from django.contrib import messages
from django.contrib.sites.models import Site
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse

from accounts.models import UserProfile


register = template.Library()



@register.inclusion_tag('includes/user_links.html', takes_context=True, name='user_links')
def create_link(context):
    if 'request' in context:
        request = context['request']
        update_profile_url = None
        user_profile = reverse('accounts-app:user-profile-custom_mixins', kwargs=({'slug': request.user}))
        profile_url = user_profile
        return {
            'profile_url': profile_url,
            'update_profile_url': update_profile_url,
            'request': request
        }


@register.simple_tag(name='admin_site_url')
def admin_site_url():
    site = Site.objects.get(id=settings.SITE_ID)
    site_domain = site.domain
    base_url_string = ''
    admin_url_string = '/admin/'
    # construct url here
    base_url_string += base_url_string.join(['/', site_domain, admin_url_string])
    return base_url_string
