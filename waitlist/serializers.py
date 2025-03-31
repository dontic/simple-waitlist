from rest_framework import serializers
from .models import Waitlist, WaitlistUser


class WaitlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waitlist
        fields = ["pk", "name"]
        read_only_fields = ["pk"]


class WaitlistUserSerializer(serializers.ModelSerializer):
    waitlist_name = serializers.CharField(write_only=True)
    waitlist = WaitlistSerializer(read_only=True)

    class Meta:
        model = WaitlistUser
        fields = ["pk", "waitlist", "waitlist_name", "email"]
        read_only_fields = ["pk", "waitlist"]

    def create(self, validated_data):
        waitlist_name = validated_data.pop("waitlist_name")
        waitlist, _ = Waitlist.objects.get_or_create(name=waitlist_name)
        validated_data["waitlist"] = waitlist
        return super().create(validated_data)
