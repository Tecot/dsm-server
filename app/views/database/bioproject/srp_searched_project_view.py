from django.http import HttpResponse
from django.views import View
import json
from app.services.database.bioproject.read_srp_searched_project_data import read_srp_searched_project_Data


class SrpSearchedProjectView(View):

    def get(self, request):
        search_data = {
            'bioProjectText': request.GET.get('bioProjectText', ''),
            'projectID': request.GET.get('projectID', ''),
            'srastudyText': request.GET.get('srastudyText', ''),
            'centerName': request.GET.get('centerName', ''),
            'submission': request.GET.get('submission', ''),
            'genes': request.GET.get('gene', ''),
            'vfs': request.GET.get('stitle', ''),
            'args': request.GET.get('sseqid', ''),
            'taxonome': request.GET.get('classification', ''),
            'product': request.GET.get('product', ''),
            'lowDepth': request.GET.get('lowDepth'),
            'highDepth': request.GET.get('highDepth'),
            'includeUnknownDepth': True if request.GET.get('includeUnknownDepth') == 'true' else False,
            'includeUnknownll': True if request.GET.get('includeUnknownll') == 'true' else False,
            's': request.GET.get('s'),
            'n': request.GET.get('n'),
            'w': request.GET.get('w'),
            'e': request.GET.get('e')
        }
        
        data = read_srp_searched_project_Data(search_data)
        response = HttpResponse(json.dumps(data), content_type='application/json')

        return response