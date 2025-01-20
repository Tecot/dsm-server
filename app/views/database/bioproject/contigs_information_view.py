from django.http import HttpResponse
from django.views import View
import json
from app.services.database.bioproject.read_contigs_information_data import read_contigs_information_data


class ContigsInformationView(View):
    
    def get(self, request, srp, current_page, page_size):
        data = read_contigs_information_data(srp, current_page, page_size)
        response = HttpResponse(json.dumps(data), content_type='application/json')
        return response