from django.http import HttpResponse
from django.views import View
import json
from app.services.database.dataexpress.read_protein_one_seq_data import read_protein_one_seq_data


class ProteinOneSeqView(View):
    
    def get(self, request, srp, code):
        data = read_protein_one_seq_data(srp, code)
        response = HttpResponse(json.dumps(data), content_type='application/json')
        return response