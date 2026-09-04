from django.db.models import Q
from .models import Profile


def search_profiles(keyword=None, skill=None, title=None):
    """
    تابع مشترک جستجو که توسط ویوهای مختلف استفاده می‌شود
    """
    queryset = Profile.objects.all()

    # جستجوی کلیدواژه
    if keyword:
        queryset = queryset.filter(
            Q(full_name__icontains=keyword) |
            Q(job_title__icontains=keyword) |
            Q(skills__icontains=keyword) |
            Q(summary__icontains=keyword)
        )

    # فیلتر مهارت (روی JSONField)
    if skill:
        queryset = queryset.filter(skills__icontains=skill)

    # فیلتر عنوان شغلی
    if title:
        queryset = queryset.filter(job_title__icontains=title)

    return queryset
