from django.contrib import admin
from .models import Waitlist, WaitlistUser


@admin.register(Waitlist)
class WaitlistAdmin(admin.ModelAdmin):
    list_display = ("name", "ntfy_topic", "created_at")
    search_fields = ("name",)


@admin.register(WaitlistUser)
class WaitlistUserAdmin(admin.ModelAdmin):
    list_display = ("email", "waitlist", "created_at")
    list_filter = ("waitlist",)
    search_fields = ("email",)
