from django.db import models

# Create your models here.


class Waitlist(models.Model):
    name = models.CharField(max_length=255, unique=True)
    ntfy_topic = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class WaitlistUser(models.Model):
    waitlist = models.ForeignKey(
        Waitlist, on_delete=models.CASCADE, related_name="users"
    )
    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.email} - {self.waitlist.name}"
