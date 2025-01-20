from django.http import HttpResponse
from django.views import View
import json
from app.services.database.bioproject.read_srp_project_data import read_srp_project_Data


class SrpProjectView(View):

    def get(self, request,current_page, page_size):
        data = read_srp_project_Data(current_page, page_size)
        response = HttpResponse(json.dumps(data), content_type='application/json')
        return response