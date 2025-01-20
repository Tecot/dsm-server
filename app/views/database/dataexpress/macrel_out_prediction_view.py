'''
File name: 
Author: Tecot (tyx_cqbs@163.com)
Version: V1.0
Date: 2024-08-13 11:55:19
Description: 
'''
from django.http import HttpResponse
from django.views import View
import json
from app.services.database.dataexpress.read_macrel_out_prediction_data import read_macrel_out_prediction_data

class MacrelOutPredictionView(View):
    
    def get(self, request, srp, current_page, page_size):
        data = read_macrel_out_prediction_data(srp, current_page, page_size)
        response = HttpResponse(json.dumps(data), content_type='application/json')
        return response