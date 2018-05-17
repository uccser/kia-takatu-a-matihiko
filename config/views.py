"""Views for the pikau application."""

from django.views import generic


class IndexView(generic.TemplateView):
    """View for the homepage that renders from a template."""

    template_name = "index.html"


class FAQView(generic.TemplateView):
    """View for the FAQ that renders from a template."""

    template_name = "faq.html"


class ContactView(generic.TemplateView):
    """View for the contact page that renders from a template."""

    template_name = "contact.html"
