from django import forms
from django.utils.translation import gettext as _

from apps.users.models import User


class CreateUserForm(forms.ModelForm):
    confirm_password = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'fullname', 'email',
                  'phone', 'address', 'address', 'password', 'confirm_password')

    def clean_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                _('Confirmation password does not match password !'))

        return password

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if User.objects.filter(phone=phone).exists():
            raise forms.ValidationError(
                _('This phone number already exists !'))

        return phone

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(phone=username).exists():
            raise forms.ValidationError(
                _('This username already exists !'))

        return username
