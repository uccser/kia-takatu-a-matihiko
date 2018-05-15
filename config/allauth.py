"""Configuration of authentication system."""

from django import forms
from django.utils.translation import ugettext_lazy
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.forms import SignupForm

VALID_EMAIL_DOMAIN = "@kiatakatu.ac.nz"
INVALID_EMAIL_MESSAGE = ugettext_lazy("Only {} emails addresses are currently allowed".format(VALID_EMAIL_DOMAIN))


class CustomAccountAdapter(DefaultAccountAdapter):
    """Custom adapter used for accounts."""

    def clean_email(self, email):
        """Validate the email value.

        Args:
            email (str): String of email address.

        Returns:
            String of valid email.
        """
        if not email.endswith(VALID_EMAIL_DOMAIN):
            raise forms.ValidationError(INVALID_EMAIL_MESSAGE)
        return email


class CustomSignupForm(SignupForm):
    """Custom registration form that includes first and last names."""

    first_name = forms.CharField(max_length=50, label="First name")
    last_name = forms.CharField(max_length=50, label="Last name")

    def signup(self, request, user):
        """Save custom form data to user.

        Args:
            request (Request): Request object.
            user (User): User object.
        """
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()
