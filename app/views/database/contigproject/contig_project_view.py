from django.http import HttpResponse
from django.views import View
import json
from app.services.database.contigproject.read_contig_project_data import read_contig_project_Data

class ContigProjectView(View):

    def get(self, request, srp, current_page, page_size):
        data = read_contig_project_Data(srp, current_page, page_size)
        response = HttpResponse(json.dumps(data), content_type='application/json')
        return response