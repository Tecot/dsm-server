from django.http import HttpResponse
from django.views import View
import json
from app.services.shared.read_srp_dir_names_data import read_srp_dir_names_data

class SrpDirNamesView(View):

    def get(self, request):
        data = read_srp_dir_names_data()
        response = HttpResponse(json.dumps(data), content_type='application/json')
        return response