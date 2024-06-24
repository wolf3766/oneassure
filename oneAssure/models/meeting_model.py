from dirtyfields import DirtyFieldsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Meeting(DirtyFieldsMixin,models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    meeting_type = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    notification_interval = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' - ' + self.description 
    
@receiver(post_save, sender=Meeting)
def schedule_notification(sender, instance, created, **kwargs):
    from ..task import send_notification_email
    if created or 'notification_interval' in instance.get_dirty_fields():
        # Schedule the task to run at the specified notification interval
        send_notification_email.apply_async((instance.id,), eta=instance.notification_interval)

