from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'job_title',
        'job_company_name',
        'location_country',
        'skills_preview'
    ]

    search_fields = [
        'full_name',
        'job_title',
        'job_company_name',
        'skills'
    ]

    list_filter = [
        'job_title_role',
        'location_country'
    ]

    list_per_page = 20

    # متد کمکی برای نمایش مهارت‌ها (چون JSON است)
    def skills_preview(self, obj):
        if obj.skills:
            # اگر لیستی از رشته‌هاست
            if isinstance(obj.skills, list) and obj.skills:
                return ", ".join(str(s)[:20] for s in obj.skills[:3])
        return "-"

    skills_preview.short_description = "مهارت‌ها"
