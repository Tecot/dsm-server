'''
File name: 
Author: Tecot (tyx_cqbs@163.com)
Version: V1.0
Date: 2024-11-21 13:10:53
Description: 
'''
# myproject/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

app = Celery('server')

# 从 Django 的 settings.py 文件中加载配置
app.config_from_object('django.conf:settings', namespace='CELERY')

# 自动发现任务模块
app.autodiscover_tasks()
