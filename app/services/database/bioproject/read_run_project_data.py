from django.conf import settings
from app.utils.detail_null_value import detail_null_value

def read_run_project_Data(srp):
    bio_project_info = list(settings.SRP_INFO)

    run_info = []

    for item in bio_project_info:
        if item['SRAStudy'] == srp:
            run_info.append({
                'Run': item['Run'],
                'LibraryStrategy': detail_null_value(item['LibraryStrategy']),
                'LibrarySelection': detail_null_value(item['LibrarySelection']),
                'LibrarySource': detail_null_value(item['LibrarySource']),
                'LibraryLayout': detail_null_value(item['LibraryLayout']),
                'Platform': detail_null_value(item['Platform']),
                'BioSample': detail_null_value(item['BioSample']),
                'geographic location': detail_null_value(item['geographic location']),
                'latitude': detail_null_value(item['latitude']),
                'longitude': detail_null_value(item['longitude']),
                'depth': detail_null_value(item['depth']),
                'collection date': detail_null_value(item['collection date'])
            })
    result = {
       'data': run_info,
       'header': [
            'Run', 
            'LibraryStrategy', 
            'LibrarySelection', 
            'LibrarySource', 
            'LibraryLayout', 
            'Platform', 
            'BioSample', 
            'geographic location',
            'latitude', 
            'longitude',
            'depth',
            'collection date'
        ]
    }

    return result

