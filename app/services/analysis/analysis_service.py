'''
File name: 
Author: Tecot (tyx_cqbs@163.com)
Version: V1.0
Date: 2024-12-11 13:31:06
Description: 
'''
'''
File name: 
Author: Tecot (tyx_cqbs@163.com)
Version: V1.0
Date: 2024-11-20 15:37:35
Description: 
'''
from django.http import JsonResponse
from datetime import datetime
from django.conf import settings
from app.models import TaskInfoModel

import os
from app.tasks.tasks import long_running_task

def analysis_service(request):
    try:
        now = datetime.now()
        str_timestamp = now.strftime("%Y_%m_%d__%H_%M_%S")
        key = 'dsm' + '-' + str_timestamp
        value = request.POST.get('name')
        request.session[key] = value

        task_dir_path = os.path.join(settings.MEDIA_ROOT, key)
        if not os.path.exists(task_dir_path):
            os.mkdir(task_dir_path)
      
        file1 = request.FILES['file1']
        sequence_file1_name = f"{key}_1{os.path.splitext(file1.name)[1]}"
        target1_data_path = os.path.join(settings.MEDIA_ROOT, key, sequence_file1_name)
        with open(target1_data_path, 'wb+') as destination:
                for chunk in file1.chunks():
                    destination.write(chunk)
        file2 = request.FILES['file2']
        sequence_file2_name = f"{key}_2{os.path.splitext(file2.name)[1]}"
        target2_data_path = os.path.join(settings.MEDIA_ROOT, key, sequence_file2_name)
        with open(target2_data_path, 'wb+') as destination:
                for chunk in file2.chunks():
                    destination.write(chunk)
        
        # 将key value 移交给数据库
        record = TaskInfoModel.objects.create(key=key, status=2)
        record.save()

        flag = request.POST.get('flag')

        # 这里是计算任务(提交给celery做异步任务)
        long_running_task.delay(key, value, settings.MEDIA_ROOT, target1_data_path, value, flag)

        response = JsonResponse({
            'code': 0, 
            'data': {
                'key': key, 
                'value': value,
                'age': settings.SESSION_COOKIE_AGE
            } 
        })
        return response
    except Exception:
        return JsonResponse({ 'code': 0, 'msg': 'Error!' })
    
