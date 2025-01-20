from django.http import HttpResponse
from django.views import View
import json
from app.services.database.bioproject.read_geo_data import read_geo_data

class GeoDataView(View):
    
    def get(self, request):
        data = read_geo_data()
        response = HttpResponse(json.dumps(data), content_type='application/json')
        return response