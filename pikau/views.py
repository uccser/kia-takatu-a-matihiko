"""Views for the pikau application."""

from django.views import generic
from pikau.models import (
    GlossaryTerm,
)


class IndexView(generic.TemplateView):
    """View for the pikau homepage that renders from a template."""

    template_name = "pikau/index.html"


class GlossaryList(generic.ListView):
    """View for the pikau application homepage."""

    template_name = "pikau/glossary.html"
    context_object_name = "glossary_terms"

    def get_queryset(self):
        """Get queryset of all glossary terms.

        Returns:
            Queryset of GlossaryTerm objects ordered by term.
        """
        return GlossaryTerm.objects.order_by("term")
