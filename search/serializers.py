from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    linkedin_url = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'full_name', 'job_title', 'skills', 'summary',
            'location_name', 'linkedin_url'
        ]

    def get_linkedin_url(self, obj):
        url = obj.linkedin_url
        if not url:
            return None
        if url.startswith(('http://', 'https://')):
            return url
        return f'https://{url}'
