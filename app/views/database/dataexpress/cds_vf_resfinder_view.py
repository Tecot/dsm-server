from django.http import HttpResponse
from django.views import View
import json
from app.services.database.dataexpress.read_cds_vf_resfinder_data import read_cds_vf_resfinder_data


class CdsVfResfinderView(View):
    
    def get(self, request, srp, contig_ID):
        data = read_cds_vf_resfinder_data(srp, contig_ID)
        response = HttpResponse(json.dumps(data), content_type='application/json')
        return response