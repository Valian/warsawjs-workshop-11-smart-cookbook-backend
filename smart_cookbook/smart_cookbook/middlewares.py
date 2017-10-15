from django.conf import settings
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin


class ApiKeyMiddleware(MiddlewareMixin):

    def process_request(self, request):
        is_debug = settings.DEBUG
        has_api_key = request.GET.get('api_key') == settings.API_KEY
        if not is_debug and not has_api_key:
            return JsonResponse({'error': "Wrong api_key query parameter"}, status=400)
