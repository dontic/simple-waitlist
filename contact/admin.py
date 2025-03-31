from django.contrib import admin
from .models import ContactList, ContactMessage
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ContactMessageResource(resources.ModelResource):
    class Meta:
        model = ContactMessage
        fields = ("id", "name", "email", "message", "contact_list")


@admin.register(ContactList)
class ContactListAdmin(admin.ModelAdmin):
    list_display = ("name", "ntfy_topic", "ntfy_email")
    search_fields = ("name",)


@admin.register(ContactMessage)
class ContactMessageAdmin(ImportExportModelAdmin):
    resource_class = ContactMessageResource
    list_display = ("name", "email", "contact_list")
    list_filter = ("contact_list",)
    search_fields = ("name", "email", "message")
