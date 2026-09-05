from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Profile


@registry.register_document
class ProfileDocument(Document):
    skills = fields.TextField()

    class Index:
        name = 'profiles'

    class Django:
        model = Profile
        fields = [
            'full_name',
            'job_title',
            'job_title_role',
            'job_company_name',
            'job_company_industry',
            'location_name',
            'location_country',
            'summary',
        ]

    def prepare_skills(self, instance):
        raw = instance.skills
        if not raw:
            return ""

        if isinstance(raw, list):
            items = []
            for item in raw:
                if isinstance(item, dict):
                    value = item.get('name') or item.get('skill') or str(item)
                    items.append(value)
                else:
                    items.append(str(item))
            return " ".join(items)

        if isinstance(raw, (int, float)):
            return str(raw)

        if isinstance(raw, str):
            return raw

        return str(raw)
