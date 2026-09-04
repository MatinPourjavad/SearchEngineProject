from rest_framework.serializers import ModelSerializer
from .models import Profile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['full_name', 'job_title', 'skills', 'summary', 'location_name', 'linkedin_url']
