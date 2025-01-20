'''
File name: 
Author: Tecot (tyx_cqbs@163.com)
Version: V1.0
Date: 2024-09-03 09:48:36
Description: 
'''
from django.conf import settings

def read_geo_data():
    items = []
    bio_project_deduplicated_info = list(settings.SRP_INFO_WITH_DEPTH_AND_LONGITUDE_AND_LATITUDE)
    for item in settings.SRP_INFO:
        latitude = item['latitude']
        new_latitude = ''
        if latitude == ' ' or latitude == '':
            new_latitude = '-'
        else:
            temps = latitude.split(' ')
            if(len(temps) == 2):
                if temps[1] == 'N':
                    new_latitude = float(temps[0])
                if temps[1] == 'S':
                    new_latitude = -float(temps[0])
        longitude = item['longitude']
        new_longitude = ' '
        if longitude == ' ' or longitude == '':
            new_longitude = '-'
        else:
            temps = longitude.split(' ')
            if len(temps) == 2:
                if temps[1] == 'E':
                    new_longitude = float(temps[0])
                if temps[1] == 'W':
                    new_longitude = -float(temps[0])
        if new_latitude != '-' and new_longitude != '-':
            srp_info = None
            for bpdi_item in bio_project_deduplicated_info:
                if item['SRAStudy'] and item['SRAStudy'] == bpdi_item['SRAStudy']:
                    srp_info = bpdi_item
                    break
            items.append({
                'name': item['SRAStudy'] if item['SRAStudy'] else '-',
                'run': item['Run'] if item['Run'] else '-',
                'depth': float(item['depth']) if item['depth'] else '-',
                'geographic location': item['geographic location'] if item['geographic location'] else 'Unkown',
                'info': srp_info,
                'value': [
                    new_longitude,
                    new_latitude,
                    float(item['depth']) if item['depth'] else -1
                ]
            })

    result = {
        'data': items
    }
    return result