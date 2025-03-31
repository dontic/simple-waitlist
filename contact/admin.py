from django.contrib import admin
from .models import ContactList, ContactMessage


@admin.register(ContactList)
class ContactListAdmin(admin.ModelAdmin):
    list_display = ("name", "ntfy_topic", "ntfy_email")
    search_fields = ("name",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "contact_list")
    list_filter = ("contact_list",)
    search_fields = ("name", "email", "message")
