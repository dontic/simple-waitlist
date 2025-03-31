import requests
import logging
from django.conf import settings

logger = logging.getLogger(__name__)


def send_ntfy_notification(topic, title, message, email=None, tags=None, actions=None):
    """
    Send a notification to NTFY service.

    Args:
        topic (str): The NTFY topic to send the notification to
        title (str): The notification title
        message (str): The notification body/message
        email (str, optional): Email address to send a copy of the notification
        tags (str, optional): Comma-separated tags for the notification
        actions (str, optional): Action buttons for the notification

    Returns:
        bool: True if notification was sent successfully, False otherwise
    """
    try:
        ntfy_url = settings.NTFY_URL
        ntfy_token = settings.NTFY_TOKEN

        if not ntfy_url or not ntfy_token:
            logger.error("Missing NTFY configuration settings")
            return False

        headers = {
            "Authorization": f"Bearer {ntfy_token}",
            "Title": title,
        }

        # Add optional headers if provided
        if email:
            headers["Email"] = email
        if tags:
            headers["Tags"] = tags
        if actions:
            headers["Actions"] = actions

        # Send the notification
        full_url = f"{ntfy_url}/{topic}"
        response = requests.post(
            full_url, data=message.encode("utf-8"), headers=headers
        )

        if response.status_code in (200, 202):
            logger.info(f"NTFY notification sent successfully to topic: {topic}")
            return True
        else:
            logger.error(
                f"Failed to send NTFY notification: HTTP {response.status_code}, {response.text}"
            )
            return False

    except Exception as e:
        logger.exception(f"Error sending NTFY notification: {str(e)}")
        return False
