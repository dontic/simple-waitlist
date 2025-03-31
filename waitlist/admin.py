from django.contrib import admin
from .models import Waitlist, WaitlistItem


@admin.register(Waitlist)
class WaitlistAdmin(admin.ModelAdmin):
    list_display = ("name", "ntfy_topic")
    search_fields = ("name",)


@admin.register(WaitlistItem)
class WaitlistItemAdmin(admin.ModelAdmin):
    list_display = ("email", "waitlist")
    list_filter = ("waitlist",)
    search_fields = ("email",)
