"""Forms for pikau application."""

from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from pikau.models import (
    GlossaryTerm
)


class GlossaryForm(ModelForm):
    """Form for pages relating to actions of glossary terms."""

    def __init__(self, *args, **kwargs):
        """Set helper for form layout."""
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("term", css_class="slug-source"),
            "description",
            "slug",
            Submit("submit", "Submit"),
        )

    class Meta:
        """Meta attributes of GlossaryForm."""

        model = GlossaryTerm
        fields = ("term", "description", "slug")
