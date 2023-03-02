from datetime import datetime


def year(request):
    dt = datetime.now().year
    return {
        'year': dt
    }
from django.utils.timezone import now


def year(request):
    return {
       'year': now().year
    }
