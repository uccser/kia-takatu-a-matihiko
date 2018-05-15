from django.db.models.signals import post_init, pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone
from pikau.models import PikauCourse


@receiver(post_init, sender=PikauCourse)
def pikau_course_post_init(sender, instance, **kwargs):
    instance.__previous_status = instance.status


@receiver(pre_save, sender=PikauCourse)
def pikau_course_pre_save(sender, instance, raw, using, update_fields, **kwargs):
    if instance.status != instance.__previous_status:
        instance.status_updated = timezone.now()


@receiver(post_save, sender=PikauCourse)
def pikau_course_post_save(sender, instance, created, raw, using, update_fields, **kwargs):
    instance.__previous_status = instance.status
