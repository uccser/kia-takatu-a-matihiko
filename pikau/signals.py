"""Django signals for pikau application."""

from django.db.models.signals import post_init, pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone
from pikau.models import PikauCourse


@receiver(post_init, sender=PikauCourse)
def pikau_course_post_init(sender, instance, **kwargs):
    """Triggered when the __init__() method finishes for PikauCourse.

    Args:
        sender (PikauCourse): PikauCourse class.
        instance (PikauCourse): The actual instance of the PikauCourse that’s just been created.
    """
    instance.__previous_status = instance.status


@receiver(pre_save, sender=PikauCourse)
def pikau_course_pre_save(sender, instance, raw, using, update_fields, **kwargs):
    """Triggered at the beginning of a model’s save() method.

    Args:
        sender (PikauCourse): PikauCourse class.
        instance (PikauCourse): The actual instance of the PikauCourse that’s just been created.
        raw (bool): True if the model is saved exactly as presented.
        using: The database alias being used.
        update_fields: The set of fields to update as passed to Model.save(),
            or None if update_fields wasn’t passed to save().
    """
    if instance.status != instance.__previous_status:
        instance.status_updated = timezone.now()


@receiver(post_save, sender=PikauCourse)
def pikau_course_post_save(sender, instance, created, raw, using, update_fields, **kwargs):
    """Triggered at the end of a model’s save() method.

    Args:
        sender (PikauCourse): PikauCourse class.
        instance (PikauCourse): The actual instance of the PikauCourse that’s just been created.
        created (bool): True if a new record was created.
        raw (bool): True if the model is saved exactly as presented.
        using: The database alias being used.
        update_fields: The set of fields to update as passed to Model.save(),
            or None if update_fields wasn’t passed to save().
    """
    instance.__previous_status = instance.status
