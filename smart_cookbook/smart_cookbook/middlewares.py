from django.conf import settings
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin


class ApiKeyMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if not settings.DEBUG:
            api_key = request.GET.get('api_key') or request.session.get('api_key')
            if api_key != settings.API_KEY:
                return JsonResponse({'error': "Wrong api_key query parameter"}, status=400)
            else:
                request.session.setdefault('api_key', api_key)
