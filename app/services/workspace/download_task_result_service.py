'''
File name: 
Author: Tecot (tyx_cqbs@163.com)
Version: V1.0
Date: 2024-12-23 13:26:52
Description: 
'''
import os
from django.http import FileResponse
from django.conf import settings
from app.services.download.zip_utils import ZipUtils

def download_task_result_service(id):
    zip_utils = ZipUtils()
    print(os.path.join(settings.DATABASE_PATH, 'media', id))
    file_open = zip_utils.zip_multiple_items([os.path.join(settings.BASE_DIR, 'media', id)], id + '.zip')
    response = FileResponse(file_open, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=' + id + '.zip'
    return response