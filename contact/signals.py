import logging
from django.db.models.signals import post_save
from django.dispatch import receiver

from utils.ntfy import send_ntfy_notification
from .models import ContactMessage

logger = logging.getLogger(__name__)


@receiver(post_save, sender=ContactMessage)
def send_contact_notification(sender, instance, created, **kwargs):
    """
    Signal handler to send notification when a new contact message is created.
    """
    if created and instance.contact_list.ntfy_topic:
        contact_list = instance.contact_list
        topic = contact_list.ntfy_topic

        # Format the message
        message_body = f"Name: {instance.name}\nEmail: {instance.email}\nMessage: {instance.message}"

        # Configure notification parameters
        notification_params = {
            "topic": topic,
            "title": "New Contact Form Submission",
            "message": message_body,
            "tags": "email",
        }

        # Add email action if email exists
        if instance.email:
            notification_params["actions"] = (
                f"view, Reply via Email, mailto:{instance.email}"
            )

        # Add ntfy_email if specified in the contact list
        if contact_list.ntfy_email:
            notification_params["email"] = contact_list.ntfy_email

        # Send the notification
        send_ntfy_notification(**notification_params)
