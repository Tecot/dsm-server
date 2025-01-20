'''
File name: 
Author: Tecot (tyx_cqbs@163.com)
Version: V1.0
Date: 2024-12-23 10:41:40
Description: 
'''
import os
from django.http import FileResponse
from django.conf import settings

def download_sample_data():
    file_path = os.path.join(settings.BASE_DIR, 'datasets/sample/SRR6787536')
    try:
        # 使用FileResponse发送文件
        # response = FileResponse(open(file_path, 'rb'), content_type='application/zip', as_attachment=True)
        # response['Content-Disposition'] = 'attachment; filename="zipfile.zip"'
        # return response
        if os.path.exists(file_path):
            response = FileResponse(open(file_path, 'rb'))
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment; filename="SRR6787536.sra"'
            return response
    except IOError as e:
        print(e)