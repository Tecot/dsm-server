'''
File name: 
Author: Tecot (tyx_cqbs@163.com)
Version: V1.0
Date: 2024-11-20 09:48:42
Description: 
'''
from django.views import View
from app.services.analysis.analysis_service import analysis_service

class AnalysisView(View):
    def post(self, request):
        return analysis_service(request)