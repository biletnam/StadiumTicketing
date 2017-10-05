from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^events$', views.EventListView.as_view(), name='event_list'),
    url(r'^event/(?P<slug>[a-zA-Z0-9-_]+)$', views.EventDetailView.as_view(), name='event_detail'),
]