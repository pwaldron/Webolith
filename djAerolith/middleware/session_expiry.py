from django.contrib.auth import logout
import datetime

import settings

class SessionIdleTimeout:
    """Middleware class to timeout a session after a specified time period.
    """
    def process_request(self, request):
        # Timeout is done only for authenticated logged in users.
        if request.user.is_authenticated():
            current_datetime = datetime.datetime.now()
            # Timeout if idle time period is exceeded.
            if (request.session.has_key('last_activity') and
                (current_datetime - request.session['last_activity']).seconds >
                    settings.SESSION_IDLE_TIMEOUT):
                logout(request)
            # Set last activity time in current session.
            else:
                request.session['last_activity'] = current_datetime
        return None