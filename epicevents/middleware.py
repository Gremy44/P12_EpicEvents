from django.shortcuts import redirect
from django.contrib import messages
from django.core.exceptions import PermissionDenied

class PermissionDeniedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 403:
            # Si la réponse est une page 403, rediriger vers la page précédente avec un message d'alerte
            referer = request.META.get('HTTP_REFERER')
            if referer:
                messages.warning(request, 'Vous n\'avez pas les autorisations nécessaires pour accéder à cette page.')
                return redirect(referer)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, PermissionDenied):
            # Si l'exception est une PermissionDenied, rediriger vers la page précédente avec un message d'alerte
            referer = request.META.get('HTTP_REFERER')
            if referer:
                messages.warning(request, 'Vous n\'avez pas les autorisations nécessaires pour accéder à cette page.')
                return redirect(referer)