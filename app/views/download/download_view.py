'''
File name: 
Author: Tecot (tyx_cqbs@163.com)
Version: V1.0
Date: 2024-12-23 10:54:32
Description: 
'''

import os
from django.http import FileResponse
from django.views import View
from django.conf import settings
from app.services.download.zip_utils import ZipUtils


class DownloadView(View):
    
    @staticmethod
    def get(request, srp):
        zip_utils = ZipUtils()
        # data_paths = [].append(os.path.join(settings.DATABASE_PATH, srp))
        file_open = zip_utils.zip_multiple_items([os.path.join(settings.DATABASE_PATH, srp)], settings.DOWNLOAD_FILE_PRENAME + '.zip')
        response = FileResponse(file_open, content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename=' + settings.DOWNLOAD_FILE_PRENAME + '.zip'
        return response