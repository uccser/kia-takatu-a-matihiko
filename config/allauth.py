from django import forms
from django.utils.translation import ugettext_lazy
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.forms import SignupForm

VALID_EMAIL_DOMAIN = "@kiatakatu.ac.nz"
INVALID_EMAIL_MESSAGE = ugettext_lazy("Only {} emails addresses are currently allowed".format(VALID_EMAIL_DOMAIN))


class CustomAccountAdapter(DefaultAccountAdapter):

    def clean_email(self, email):
        """Validates the email value.

        Args:
            email (str): String of email address.

        Returns:
            String of valid email.
        """
        if not email.endswith(VALID_EMAIL_DOMAIN):
            raise forms.ValidationError(INVALID_EMAIL_MESSAGE)
        return email


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=50, label="First name")
    last_name = forms.CharField(max_length=50, label="Last name")

    def signup(self, request, user):
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()
