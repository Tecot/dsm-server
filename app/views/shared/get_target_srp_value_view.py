from django.http import HttpResponse
from django.views import View
import json
from app.services.shared.get_target_srp_value import get_target_srp_value

class GetTargetSrpValueView(View):

    def get(self, request, srp):
        data = get_target_srp_value(srp)
        response = HttpResponse(json.dumps(data), content_type='application/json')
        return response