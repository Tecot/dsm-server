from django.http import HttpResponse
from django.views import View
import json
from app.services.database.dataexpress.read_protein_seq_data import read_protein_seq_data


class ProteinSeqView(View):
    
    def get(self, request, srp):
        data = read_protein_seq_data(srp)
        response = HttpResponse(json.dumps(data), content_type='application/json')
        return response