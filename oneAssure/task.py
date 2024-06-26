from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_notification_email(meeting_id):
    from .models import Meeting

    meeting = Meeting.objects.get(id=meeting_id)

    if meeting.start_time < meeting.user_id.dnd_start_time or meeting.start_time > meeting.user_id.dnd_end_time:
        return

    send_mail(
        'Meeting Notification',
        f'Reminder: Your meeting "{meeting.title}" is scheduled at {meeting.start_time}.',
        'skc@oneassure.com',
        [meeting.user_id.email],
        fail_silently=False,
    )
