'''
File name: 
Author: Tecot (tyx_cqbs@163.com)
Version: V1.0
Date: 2024-12-11 15:14:11
Description: 
'''
'''
File name: 
Author: Tecot (tyx_cqbs@163.com)
Version: V1.0
Date: 2024-12-11 15:14:06
Description: 
'''
import json
from django.http import HttpResponse
from django.views import View
from app.services.workspace.get_task_statuses_service import get_task_statuses_service

class TaskStatuses(View):
    @staticmethod
    def get(request, keys_str):
        data = get_task_statuses_service(keys_str)
        response = HttpResponse(json.dumps(data), content_type='application/json')
        return response