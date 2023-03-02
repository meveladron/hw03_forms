from datetime import datetime


def year(request):
    return {
      request, datetime.now().date()
    }
