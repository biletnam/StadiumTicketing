"""Contains all views of `events` app"""

from django.views.generic import TemplateView
from helpers.mixins import TitleMixin


class IndexView(TitleMixin, TemplateView):
    """Entry point view"""
    template_name = 'index.html'
    title = 'Index'
