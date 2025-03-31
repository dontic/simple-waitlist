from django.contrib import admin
from .models import Waitlist, WaitlistUser
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class WaitlistUserResource(resources.ModelResource):
    class Meta:
        model = WaitlistUser
        fields = ("id", "email", "waitlist", "created_at")


@admin.register(Waitlist)
class WaitlistAdmin(admin.ModelAdmin):
    list_display = ("name", "ntfy_topic", "created_at")
    search_fields = ("name",)


@admin.register(WaitlistUser)
class WaitlistUserAdmin(ImportExportModelAdmin):
    resource_class = WaitlistUserResource
    list_display = ("email", "waitlist", "created_at")
    list_filter = ("waitlist",)
    search_fields = ("email",)
