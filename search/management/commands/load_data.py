import csv
from ast import literal_eval
from django.core.management.base import BaseCommand
from search.models import Profile  # اسم اپ خودت رو جایگزین کن


def clean_str(value):
    if value and isinstance(value, str):
        return value.strip()
    return None


def safe_literal_eval(value):
    if not value or not isinstance(value, str):
        return []
    try:
        return literal_eval(value)
    except (ValueError, SyntaxError):
        return []


def safe_float(value):
    if value is None or value == '':
        return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


class Command(BaseCommand):
    help = 'Load LinkedIn dataset from CSV into database'

    def handle(self, *args, **kwargs):
        file_path = 'data/linkedin_dataset.csv'  # مسیر درست رو بذار

        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            # 🔍 دیباگ: چاپ هدرها برای اطمینان
            self.stdout.write(f"📋 ستون‌های موجود: {reader.fieldnames}")

            profiles = []

            for row in reader:
                # فیلدهای JSON-like
                skills = safe_literal_eval(row.get('skills'))
                experience = safe_literal_eval(row.get('experience'))
                education = safe_literal_eval(row.get('education'))
                job_title_levels = safe_literal_eval(row.get('job_title_levels'))
                emails = safe_literal_eval(row.get('emails'))
                phone_numbers = safe_literal_eval(row.get('phone_numbers'))

                profile = Profile(
                    full_name=clean_str(row.get('full_name')),
                    first_name=clean_str(row.get('first_name')),
                    last_name=clean_str(row.get('last_name')),
                    gender=clean_str(row.get('gender')),
                    linkedin_url=clean_str(row.get('linkedin_url')),
                    linkedin_username=clean_str(row.get('linkedin_username')),
                    linkedin_id=clean_str(row.get('linkedin_id')),
                    job_title=clean_str(row.get('job_title')),
                    job_title_role=clean_str(row.get('job_title_role')),
                    job_title_levels=job_title_levels,
                    job_company_name=clean_str(row.get('job_company_name')),
                    job_company_industry=clean_str(row.get('job_company_industry')),
                    job_company_location_name=clean_str(row.get('job_company_location_name')),
                    location_name=clean_str(row.get('location_name')),
                    location_region=clean_str(row.get('location_region')),
                    location_country=clean_str(row.get('location_country')),
                    skills=skills,
                    experience=experience,
                    education=education,
                    summary=clean_str(row.get('summary')),
                    # ✅ استفاده از safe_float برای فیلدهای عددی
                    inferred_years_experience=safe_float(row.get('inferred_years_experience')),
                    linkedin_connections=safe_float(row.get('linkedin_connections')),
                    emails=emails,
                    phone_numbers=phone_numbers,
                )
                profiles.append(profile)

            # ذخیره یکجا
            Profile.objects.bulk_create(profiles)
            self.stdout.write(self.style.SUCCESS(f'✅ Successfully loaded {len(profiles)} profiles'))