from django.http import HttpResponse
from django.views import View
import json
from app.services.database.bioproject.read_contigs_searched_information_data import read_contigs_searched_information_data

class ContigsSearchedInformationView(View):
    
    def get(self, request):
        search_data = {
            'name': request.GET.get('name'),
            'id': request.GET.get('id'),
            'description': request.GET.get('description'),
            'lengthLow': request.GET.get('lengthLow'),
            'lengthHigh': request.GET.get('lengthHigh'),
            'gcLow': request.GET.get('gcLow'),
            'gcHigh': request.GET.get('gcHigh'),
            'srp': request.GET.get('srp'),
            'currentPage': request.GET.get('currentPage'),
            'pageSize': request.GET.get('pageSize')
        }
        data = read_contigs_searched_information_data(search_data)
        response = HttpResponse(json.dumps(data), content_type='application/json')
        return response