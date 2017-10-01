from django.views.generic import TemplateView
from helpers.mixins import TitleMixin


class IndexView(TitleMixin, TemplateView):
    template_name = 'events/index.html'
    title = 'Index'