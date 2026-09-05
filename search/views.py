from django.views.generic import TemplateView
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from .services import search_profiles
from .serializers import ProfileSerializer


class SearchAPIView(APIView):
    def get(self, request):
        keyword = request.GET.get('q', '').strip()
        skill = request.GET.get('skill', '').strip()
        title = request.GET.get('title', '').strip()
        country = request.GET.get('country', '').strip()
        industry = request.GET.get('industry', '').strip()

        queryset = search_profiles(keyword, skill, title, country, industry)

        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(queryset, request, view=self)

        serializer = ProfileSerializer(page, many=True)

        return paginator.get_paginated_response(serializer.data)


class HomeView(TemplateView):
    template_name = 'search/index.html'
