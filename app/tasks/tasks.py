'''
File name: 
Author: Tecot (tyx_cqbs@163.com)
Version: V1.0
Date: 2024-11-21 15:07:35
Description: 
'''
from celery import shared_task
import subprocess
import os
from django.conf import settings
from app.models import TaskInfoModel

@shared_task
def long_running_task(key, value, task_dir, target_data, task, flag):
    shell_path = os.path.join(settings.BASE_DIR, 'app', 'shell', 'all.sh')
    user = key
    arguments = [task_dir, user, target_data, task, flag]
    result = subprocess.run([shell_path] + arguments, shell=False)
    try:
        if result.returncode == 0:
            task = TaskInfoModel.objects.get(key=key)
            task.status = 0
            task.save()
        else:
            task = TaskInfoModel.objects.get(key=key)
            task.status = 1 # 流程程序出错
            task.save()
    except Exception as e:
        task = TaskInfoModel.objects.get(key=key)
        task.status = 1 # 流程程序出错
        task.save()
    return f"Task {key} with value {value} completed."