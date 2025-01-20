import os
from django.conf import settings
from app.utils.read_csv_as_objects import read_csv_as_objects

# 处理深度数组：将深度数组处理成一个范围字符串，例如 '123~324'
def detail_dethes_to_range(depthes=[]):
    depth_range = '-'
    depthes_delete_temp_str = [x for x in depthes if x != '']
    if len(depthes_delete_temp_str):
        depthes_float_list = [float(x) for x in depthes_delete_temp_str]
        min_depth = min(depthes_float_list)
        max_depth = max(depthes_float_list)
        if min_depth == max_depth:
            depth_range = min_depth
        else:
            depth_range = str(min_depth) + '~' + str(max_depth)
    return depth_range

# 处理经度
def detail_longitudes_to_range(longitudes):
    longitudes_range = '-'
    longitudes_delete_temp_str = [x for x in longitudes if x != '']
    if len(longitudes_delete_temp_str):
        if all(item == longitudes_delete_temp_str[0] for item in longitudes_delete_temp_str):
            longitudes_range = longitudes_delete_temp_str[0]
        else:
            max_W_longitude = 9999
            min_W_longitude = 9999
            max_E_longitude = 9999
            min_E_longitude = 9999
            w_flag = True
            e_flag = True
            for item in longitudes_delete_temp_str:
                longitude, forward= item.split(' ')

                if forward == 'W':
                    if w_flag:
                        max_W_longitude = float(longitude)
                        min_W_longitude = float(longitude)
                        w_flag = False
                    else:
                        if float(longitude) > max_W_longitude:
                            max_W_longitude = float(longitude)
                        if float(longitude) < min_W_longitude:
                            min_W_longitude = float(longitude)
                if forward == 'E':
                    if e_flag:
                        max_E_longitude = float(longitude)
                        min_E_longitude = float(longitude)
                        e_flag = False
                    else:
                        if float(longitude) > max_E_longitude:
                            max_E_longitude = float(longitude)
                        if float(longitude) < min_E_longitude:
                            min_E_longitude = float(longitude)
            
            if max_W_longitude != 9999 and min_W_longitude != 9999 and max_E_longitude != 9999 and min_E_longitude != 9999:
                longitudes_range = str(max_W_longitude) + ' W~' + str(max_E_longitude) + ' E'

            if max_W_longitude != 9999 and min_W_longitude != 9999 and max_E_longitude == 9999 and min_E_longitude == 9999:
                if min_W_longitude == max_W_longitude:
                    longitudes_range = str(max_W_longitude) + ' W'
                else:
                    longitudes_range = str(min_W_longitude) + ' W~' + str(max_W_longitude) + ' W'
            
            if max_W_longitude == 9999 and min_W_longitude == 9999 and max_E_longitude != 9999 and min_E_longitude != 9999:
                if min_E_longitude == max_E_longitude:
                    longitudes_range = str(max_E_longitude) + ' E'
                else:
                    longitudes_range = str(min_E_longitude) + ' E~' + str(max_E_longitude) + ' E'     
    return longitudes_range

# 处理纬度
def detail_latitudes_to_range(longitudes):
    latitudes_range = '-'
    latitudes_delete_temp_str = [x for x in longitudes if x != '']
    if len(latitudes_delete_temp_str):
        if all(item == latitudes_delete_temp_str[0] for item in latitudes_delete_temp_str):
            latitudes_range = latitudes_delete_temp_str[0]
        else:
            max_S_latitude = 9999
            min_S_latitude = 9999
            max_N_latitude = 9999
            min_N_latitude = 9999
            s_flag = True
            n_flag = True

            for item in latitudes_delete_temp_str:
                latitude, forward = item.split(' ')
                if forward == 'S':
                    if s_flag:
                        max_S_latitude = float(latitude)
                        min_S_latitude = float(latitude)
                        s_flag = False
                    else:
                        if float(latitude) > max_S_latitude:
                            max_S_latitude = float(latitude)
                        if float(latitude) < min_S_latitude:
                            min_S_latitude = float(latitude)
                if forward == 'N':
                    if n_flag:
                        max_N_latitude = float(latitude)
                        min_N_latitude = float(latitude)
                        n_flag = False
                    else:
                        if float(latitude) > max_N_latitude:
                            max_N_latitude = float(latitude)
                        if float(latitude) < min_N_latitude:
                            min_N_latitude = float(latitude)
            
            if max_S_latitude != 9999 and min_S_latitude != 9999 and max_N_latitude != 9999 and min_N_latitude != 9999:
                latitudes_range = str(max_S_latitude) + ' S~' + str(max_N_latitude) + ' N'

            if max_S_latitude != 9999 and min_S_latitude != 9999 and max_N_latitude == 9999 and min_N_latitude == 9999:
                if min_S_latitude == max_S_latitude:
                    latitudes_range = str(max_S_latitude) + ' S'
                else:
                    latitudes_range = str(min_S_latitude) + ' S~' + str(max_S_latitude) + ' S'
            
            if max_S_latitude == 9999 and min_S_latitude == 9999 and max_N_latitude != 9999 and min_N_latitude != 9999:
                if min_N_latitude == max_N_latitude:
                    latitudes_range = str(max_N_latitude) + ' N'
                else:
                    latitudes_range = str(min_N_latitude) + ' N~' + str(max_N_latitude) + ' N'
    return latitudes_range

def read_detailed_sra_info():
    SRP_INFO = settings.SRP_INFO
    temp = []
    result = []

    # 提取SRPStudey
    sraStudiesSet = set()
    for item in SRP_INFO:
        sraStudiesSet.add(item['SRAStudy'])
    sraStudies = list(sraStudiesSet)

    for sraStudy in sraStudies:
        # 维度       经度       深度       SRP对象    判断是否记录SRP对象信息
        longitudes, latitudes, depthes, sraStudyInfo, flag = [], [], [], {}, True
        for srp in SRP_INFO:
            if sraStudy == srp['SRAStudy']:
                if flag:
                    sraStudyInfo = {
                        'SRAStudy': srp['SRAStudy'],
                        'BioProject': srp['BioProject'],
                        'ProjectID': srp['ProjectID'],
                        'CenterName': srp['CenterName'],
                        'Submission': srp['Submission']
                    }
                    flag = False
                latitudes.append(srp['latitude'])
                longitudes.append(srp['longitude'])
                depthes.append(srp['depth'])

        # 深度(depth)处理
        sraStudyInfo['Depth range'] = detail_dethes_to_range(depthes)
        # 经纬度处理
        longitude_latitude_range = ''
        # 处理经度
        longitude_range = detail_longitudes_to_range(longitudes)
        latitude_range = detail_latitudes_to_range(latitudes)
        if longitude_range == '-' and latitude_range == '-':
            longitude_latitude_range = '-'
        elif longitude_range != '-' and latitude_range == '-':
            longitude_latitude_range = longitude_range
        elif longitude_range == '-' and latitude_range != '-':
            longitude_latitude_range = latitude_range
        else:
            longitude_latitude_range = longitude_range + ';' + latitude_range
            
        sraStudyInfo['Longitude and latitude range'] = longitude_latitude_range

        temp.append(sraStudyInfo)
    
    # 合并基因等信息
    deduplicated_info = read_csv_as_objects(os.path.join(settings.DATABASE_PATH, settings.SRP_DEDUPLICATED_INFO_FILE))
    deduplicated_key_struct_info = {}
    for di in deduplicated_info:
        deduplicated_key_struct_info[di['SRAStudy']] = {
            'genes': di['genes'],
            'vfs': di['vfs'],
            'args': di['args'],
            'taxonome': di['taxonome'],
            'product': di['product'],
            'amps': di['amps']
        }
    
    for item in temp:
        tempItem = item
        tempItem['genes'] = ''
        tempItem['vfs'] = ''
        tempItem['args'] = ''
        tempItem['taxonome'] = ''
        tempItem['product'] = ''
        tempItem['amps'] = ''
        if item['SRAStudy'] in deduplicated_key_struct_info:
            tempItem['genes'] = deduplicated_key_struct_info[item['SRAStudy']]['genes']
            tempItem['vfs'] = deduplicated_key_struct_info[item['SRAStudy']]['vfs']
            tempItem['args'] = deduplicated_key_struct_info[item['SRAStudy']]['args']
            tempItem['taxonome'] = deduplicated_key_struct_info[item['SRAStudy']]['taxonome']
            tempItem['product'] = deduplicated_key_struct_info[item['SRAStudy']]['product']
            tempItem['amps'] = deduplicated_key_struct_info[item['SRAStudy']]['amps']
        result.append(tempItem)

    return result