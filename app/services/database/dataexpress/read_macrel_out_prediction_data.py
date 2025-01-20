'''
File name: 
Author: Tecot (tyx_cqbs@163.com)
Version: V1.0
Date: 2024-08-13 11:09:01
Description: 
'''
import os
from django.conf import settings

def read_macrel_out_prediction_data(srp, current_page, page_size):
    file_path = os.path.join(settings.DATABASE_PATH, srp, settings.MACREL_OUT_PREDICTION_FILE)
    dicts = []
    with open(file_path, 'r') as file:
        content_str = file.read()
        contents = content_str.split('\n')
        headers = contents[0].split('\t')
        data = contents[1:]
        for item_str in data:
            items = item_str.split('\t')
            if items[0] != '':
                obj = {}
                for i in range(0, len(headers)):
                    obj[headers[i]] = items[i]
                    # 包含'Sequence'字段
                dicts.append(obj)
    total = len(dicts) 
    header = list(dicts[0].keys())
    slice_data = []

    if total - page_size * current_page > page_size:
        slice_data = dicts[page_size * (current_page - 1) : page_size * current_page]
    else:
        slice_data = dicts[page_size * (current_page - 1) : total]
    
    result = {
        'header': header,
        'data': slice_data,
        'total': total
    }
    
    return result   