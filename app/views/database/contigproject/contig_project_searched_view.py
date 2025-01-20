from django.http import HttpResponse
from django.views import View
import json
from app.services.database.contigproject.read_contig_project_searched_data import read_contig_project_searched_Data

class ContigProjectSearchedView(View):

    def get(self, request):
        search_data = {
            'srp': request.GET.get('srp'),
            'currentPage': request.GET.get('currentPage'),
            'pageSize': request.GET.get('pageSize'),
            'name': request.GET.get('name'),
            'id': request.GET.get('id'),
            'description': request.GET.get('description'),
            'lengthLow': request.GET.get('lengthLow'),
            'lengthHigh': request.GET.get('lengthHigh'),
            'gcLow': request.GET.get('gcLow'),
            'gcHigh': request.GET.get('gcHigh'),
            'stitle': request.GET.get('stitle'),
            'sseqid': request.GET.get('sseqid'),
            'genes': request.GET.get('genes'),
            'bin': request.GET.get('bin'),
            'classification': request.GET.get('classification'),
            'product': request.GET.get('product'),
            'ifSearchStitleUnknown': request.GET.get('ifSearchStitleUnknown'),
            'ifSearchSseqidUnknown': request.GET.get('ifSearchSseqidUnknown'),
            'ifSearchGenesUnknown': request.GET.get('ifSearchGenesUnknown'),
            'ifSearchBinUnknown': request.GET.get('ifSearchBinUnknown'),
            'ifSearchClassificationUnknown': request.GET.get('ifSearchClassificationUnknown'),
            'ifSearchProductUnknown': request.GET.get('ifSearchProductUnknown')
        }
        data = read_contig_project_searched_Data(search_data)
        response = HttpResponse(json.dumps(data), content_type='application/json')

        return response