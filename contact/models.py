from django.db import models


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
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        ordering = ["-created_at"]
