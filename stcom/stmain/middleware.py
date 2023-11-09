

from django.http import HttpResponseNotFound
from django.urls import resolve

class RestrictAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated and is a superuser
        if request.user.is_authenticated and request.user.is_superuser:
            # Allow access to the admin panel
            return self.get_response(request)
        else:
            # Return a 404 response for non-superusers
            return HttpResponseNotFound("Page not found")
