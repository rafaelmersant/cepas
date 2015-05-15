from datetime import datetime
from django.http import HttpResponseRedirect


class SessionExpiredMiddleware:

    def process_request(self, request):
        request.session.set_expiry(1500)
