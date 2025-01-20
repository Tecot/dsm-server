'''
File name: 
Author: Tecot (tyx_cqbs@163.com)
Version: V1.0
Date: 2024-11-20 10:42:54
Description: 
'''
"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.wsgi import get_wsgi_application
from django.contrib.sessions.models import Session
from django.conf import settings
from datetime import datetime, timedelta
import shutil

scheduler = BackgroundScheduler()
@scheduler.scheduled_job(trigger='interval', days=1, start_date='2024-11-20 10:00:00', id='clear_session')
def clear_session_job():
    expiry_date = datetime.now() - timedelta(seconds=settings.SESSION_COOKIE_AGE)
    # 查询过期的session
    expired_sessions = Session.objects.filter(expire_date__lt=expiry_date)

    # 可以打印出来看看
    for session in expired_sessions:
        path = os.path.join(settings.MEDIA_ROOT, session.session_value)
        if os.path.exists(path):
            shutil.rmtree(path)
    os.system('python manage.py clearsessions')
scheduler.start()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()
