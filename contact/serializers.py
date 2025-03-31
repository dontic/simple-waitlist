from rest_framework import serializers
from .models import ContactList, ContactMessage


class ContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactList
        fields = ["pk", "name"]
        read_only_fields = ["pk"]


class ContactMessageSerializer(serializers.ModelSerializer):
    contact_list_name = serializers.CharField(write_only=True, required=False)
    contact_list = ContactListSerializer(read_only=True)

    class Meta:
        model = ContactMessage
        fields = ["pk", "contact_list", "contact_list_name", "name", "email", "message"]
        read_only_fields = ["pk", "contact_list"]

    def create(self, validated_data):
        contact_list_name = validated_data.pop("contact_list_name")
        contact_list, _ = ContactList.objects.get_or_create(name=contact_list_name)
        validated_data["contact_list"] = contact_list
        return super().create(validated_data)
