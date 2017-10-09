from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<slug>[a-zA-Z0-9-]+)$', views.UserProfileView.as_view(), name="userprofile_detail"),
    url(r'^update/(?P<slug>[a-zA-Z0-9-]+)$', views.UpdateUserProfileView.as_view(), name="userprofile_update"),
]