from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import UserProfile


class UserProfileAdmin(UserAdmin):
    fieldsets = [
        # ----------------------------------------------------------------------------
        # -------------------DO NOT REMOVE OR ALTER ANYTHING--------------------------
        # You may add fields you added in the UserProfile model so that they may appear
        # in the administration site.
        # -----------------------------------------------------------------------------
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('profile_picture', 'first_name', 'last_name', 'email', 'phone_number')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    ]


admin.site.register(UserProfile, UserProfileAdmin)
