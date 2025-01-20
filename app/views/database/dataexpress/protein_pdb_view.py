from django.http import HttpResponse
from django.views import View
import json
from app.services.database.dataexpress.read_protein_pdb_data import read_protein_pdb_data


class ProteinPdbView(View):
    
    @staticmethod
    def get(request, srp, code):
        data = read_protein_pdb_data(srp, code)
        response = HttpResponse(json.dumps(data), content_type='application/json')
        return response