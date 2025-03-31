from django.db import models

# Create your models here.


class Waitlist(models.Model):
    name = models.CharField(max_length=255, unique=True)
    ntfy_topic = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class WaitlistItem(models.Model):
    waitlist = models.ForeignKey(
        Waitlist, on_delete=models.CASCADE, related_name="items"
    )
    email = models.EmailField()

    def __str__(self):
        return f"{self.email} - {self.waitlist.name}"
