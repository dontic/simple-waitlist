from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_superuser(apps, schema_editor):
    User = apps.get_model("authentication", "User")
    User.objects.create(
        username="admin",
        password=make_password("admin"),
        is_staff=True,
        is_superuser=True,
        is_active=True,
        email="admin@example.com",
    )


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
