"""Forms for files application."""

from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from files.models import (
    File
)


class FileForm(ModelForm):
    """Form for pages relating to actions of files."""

    def __init__(self, *args, **kwargs):
        """Set helper for form layout."""
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("filename", css_class="slug-source"),
            "description",
            "location",
            "licence",
            "slug",
            Submit("submit", "Submit"),
        )

    class Meta:
        """Meta attributes of GlossaryForm."""

        model = File
        fields = (
            "filename",
            "description",
            "location",
            "licence",
            "slug",
        )
