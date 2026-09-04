from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .services import search_profiles
from .serializers import ProfileSerializer


class SearchAPIView(APIView):
    """
    API جستجو - خروجی JSON
    """
    def get(self, request):
        keyword = request.GET.get('q', '').strip()
        skill = request.GET.get('skill', '').strip()
        title = request.GET.get('title', '').strip()

        queryset = search_profiles(keyword, skill, title)
        serializer = ProfileSerializer(queryset, many=True)

        return Response(serializer.data)


# class HomeView(TemplateView):
#     """
#     صفحه اصلی با فرم جستجو
#     """
#     template_name = 'search/index.html'
#