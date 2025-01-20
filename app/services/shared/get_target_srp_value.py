import os
from django.conf import settings

def get_target_srp_value(srp):
    bio_project_deduplicated_info = list(settings.SRP_INFO_WITH_DEPTH_AND_LONGITUDE_AND_LATITUDE)
    value = None
    for item in bio_project_deduplicated_info: 
        if item['SRAStudy'] == srp:
            value = item
            break
    result = {
        'data': value
    }

    return result