from django.forms import ModelForm, ValidationError
from django.utils.text import slugify
from pikau.models import Topic

class TopicForm(ModelForm):
    """Base form for editing a topic."""

    class Meta:
        model = Topic
        fields = ["name"]

    def save(self):
        instance = super().save(commit=False)
        slug = slugify(instance.name)
        if Topic.objects.filter(slug=slug):
            raise ValidationError("Topic already exists with matching slug, please change topic name")
        instance.slug = slug
        instance.save()
        return instance
