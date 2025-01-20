'''
File name: 
Author: Tecot (tyx_cqbs@163.com)
Version: V1.0
Date: 2024-12-23 10:42:32
Description: 
'''
from django.views import View
from app.services.shared.download_sample_data import download_sample_data

class DownloadSampleDataView(View):
    def get(self, request):
        return download_sample_data()