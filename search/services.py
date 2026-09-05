from .documents import ProfileDocument
from .models import Profile
from elasticsearch_dsl import Q


def search_profiles(keyword=None, skill=None, title=None, country=None, industry=None):
    s = ProfileDocument.search()
    must_conditions = []
    filter_conditions = []

    if keyword:
        must_conditions.append(
            Q('multi_match',
              query=keyword,
              fields=['full_name', 'job_title', 'skills', 'summary'],
              fuzziness='AUTO')
        )

    if skill:
        filter_conditions.append(Q('match', skills=skill))
    if title:
        filter_conditions.append(Q('match', job_title=title))
    if country:
        filter_conditions.append(Q('match', location_country=country))
    if industry:
        filter_conditions.append(Q('match', job_company_industry=industry))

    if must_conditions or filter_conditions:
        s = s.query('bool', must=must_conditions, filter=filter_conditions)

    response = s.execute()

    profiles = []
    for hit in response:
        try:
            profile = Profile.objects.get(id=hit.meta.id)
            profiles.append(profile)
        except Profile.DoesNotExist:
            continue

    return profiles
