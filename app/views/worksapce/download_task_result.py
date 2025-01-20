'''
File name: 
Author: Tecot (tyx_cqbs@163.com)
Version: V1.0
Date: 2024-12-24 10:17:57
Description: 
'''
import json
from django.http import HttpResponse
from django.views import View
from app.services.workspace.download_task_result_service import download_task_result_service

class DownloadTaskResultView(View):
    def get(self, request, id):
        return download_task_result_service(id)