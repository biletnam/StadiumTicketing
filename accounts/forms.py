from django import forms
from .models import UserProfile


class CreateUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name',
                  'last_name',
                  'profile_picture',
                  'phone_number')

    def clean_first_name(self):
        fn = self.cleaned_data['first_name']
        for char in fn:
            if not char.isalpha():
                raise forms.ValidationError("Digits are not allowed.")
        return fn

    def clean_last_name(self):
        fn = self.cleaned_data['last_name']
        for char in fn:
            if not char.isalpha():
                raise forms.ValidationError("Digits are not allowed.")
        return fn
