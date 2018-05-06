"""Views for the pikau application."""

from django.views import generic


class IndexView(generic.TemplateView):
    """View for the pikau homepage that renders from a template."""

    template_name = "index.html"


class FAQView(generic.TemplateView):
    """View for the pikau FAQ that renders from a template."""

    template_name = "faq.html"
