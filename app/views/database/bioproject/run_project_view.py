from django.http import HttpResponse
from django.views import View
import json
from app.services.database.bioproject.read_run_project_data import read_run_project_Data

class RunProjectView(View):
    
    def get(self, request, srp):
        data = read_run_project_Data(srp)
        response = HttpResponse(json.dumps(data), content_type='application/json')
        return response