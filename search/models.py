from django.db import models


class Profile(models.Model):

    full_name = models.CharField(max_length=255, db_index=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    linkedin_username = models.CharField(max_length=100, blank=True, null=True)
    linkedin_id = models.CharField(max_length=50, blank=True, null=True)

    job_title = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    job_title_role = models.CharField(max_length=100, blank=True, null=True)
    job_title_levels = models.JSONField(default=list)  # مثلاً ['manager']
    job_company_name = models.CharField(max_length=255, blank=True, null=True)
    job_company_industry = models.CharField(max_length=255, blank=True, null=True)
    job_company_location_name = models.CharField(max_length=255, blank=True, null=True)

    location_name = models.CharField(max_length=255, blank=True, null=True)
    location_region = models.CharField(max_length=100, blank=True, null=True)
    location_country = models.CharField(max_length=100, blank=True, null=True)

    skills = models.JSONField(default=list)

    experience = models.JSONField(default=list)
    education = models.JSONField(default=list)

    summary = models.TextField(blank=True, null=True)
    inferred_years_experience = models.FloatField(blank=True, null=True)
    linkedin_connections = models.FloatField(blank=True, null=True)

    emails = models.JSONField(default=list)
    phone_numbers = models.JSONField(default=list)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['full_name']),
            models.Index(fields=['job_title']),
            models.Index(fields=['location_country']),
        ]

    def __str__(self):
        return self.full_name or f"Profile {self.id}"
