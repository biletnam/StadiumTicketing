from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView
from .forms import CreateUserProfileForm
from .models import UserProfile
from . import mixins


class UserProfileView(LoginRequiredMixin, mixins.CheckIfProfileExist, DetailView):
    model = UserProfile
    template_name = 'accounts/userprofile_detail.html'
    slug_field = 'username'

    def get_context_data(self, **kwargs):
        c = super(UserProfileView, self).get_context_data(**kwargs)
        user = UserProfile.objects.get(username=self.request.user)
        c['profile'] = user
        return c


class UpdateUserProfileView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = CreateUserProfileForm
    template_name = 'accounts/update_profile.html'
    slug_field = 'username'

    def get_success_url(self):
        messages.success(self.request, 'Profile successfully updated.')
        return reverse('userprofile:userprofile_detail', kwargs=({'slug': self.request.user.username, }))
