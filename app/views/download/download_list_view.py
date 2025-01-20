from django.http import HttpResponse
from django.views import View
import json
from app.services.download.read_download_list_data import read_download_list_data


class DownloadListView(View):

    def get(self, request, current_page, page_size):
        data = read_download_list_data(current_page, page_size)
        response = HttpResponse(json.dumps(data), content_type='application/json')
        return response