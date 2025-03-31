import logging
from django.db.models.signals import post_save
from django.dispatch import receiver

from utils.ntfy import send_ntfy_notification
from .models import WaitlistUser

logger = logging.getLogger(__name__)


@receiver(post_save, sender=WaitlistUser)
def send_waitlist_notification(sender, instance, created, **kwargs):
    """
    Signal handler to send notification when a new user joins a waitlist.
    """
    if created and instance.waitlist.ntfy_topic:
        waitlist = instance.waitlist
        topic = waitlist.ntfy_topic

        # Format the message
        message_body = f"Email: {instance.email}\nWaitlist: {waitlist.name}"

        # Configure notification parameters
        notification_params = {
            "topic": topic,
            "title": "New Waitlist Signup",
            "message": message_body,
            "tags": "user,signup",
        }

        # Send the notification
        send_ntfy_notification(**notification_params)
