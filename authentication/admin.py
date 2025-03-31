from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.admin import ModelAdmin

from .models import User


# Register User model with the admin site
@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass
