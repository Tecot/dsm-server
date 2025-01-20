from django.http import HttpResponse
from django.views import View
import json
from app.services.database.dataexpress.read_bin_data import read_bin_data


class BinView(View):
    
    def get(self, request, srp):
        data = read_bin_data(srp)
        response = HttpResponse(json.dumps(data), content_type='application/json')
        return response