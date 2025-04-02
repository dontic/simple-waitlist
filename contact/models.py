from django.db import models
from django.db.models import JSONField


class ContactList(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ntfy_topic = models.CharField(max_length=100, blank=True, null=True)
    ntfy_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    contact_list = models.ForeignKey(
        ContactList, on_delete=models.CASCADE, related_name="messages"
    )
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField(blank=True)
    other_fields = JSONField(blank=True, default=dict)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        ordering = ["-created_at"]
