from datetime import datetime
from django.http import HttpResponseRedirect

class SessionExpiredMiddleware:

    def process_request(self, request):
    	pass

        # last_activity = request.session['last_activity'] if request.session.has_key('last_activity') else datetime.now()
        # now = datetime.now()

        # sincetime = now - datetime.strptime(last_activity[:19], '%Y-%m-%d %H:%M:%S')
        # if int(sincetime.total_seconds() /60) > 1:

        # 	pass
        #     # Do logout / expire session
        #     # and then...
        #     # return HttpResponseRedirect("/accounts/login/")

        # if not request.is_ajax():
        #     request.session['last_activity'] = str(now)

