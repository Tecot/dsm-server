from django.conf import settings

# 判断深度，如果在范围内返回True，否则返回False
def check_depth(depth_range, low_depth, high_depth, include_known = False):
    new_depth_range = str(depth_range)
    if new_depth_range == '-':
        return include_known
    else:
        if '~' in new_depth_range:
            low_depth_str, high_depth_str = new_depth_range.split('~')
            float_low_depth = float(low_depth_str)
            float_high_depth = float(high_depth_str)
            if low_depth <= float_low_depth and float_high_depth <= high_depth:
                return True
            else:
                return False
        else:
            float_depth = float(new_depth_range)
            if low_depth <= float_depth and float_depth <= high_depth:
                return True
            else:
                return False

# 判断单字段
def checkSingleField(target, source):
    if target == '':
        return True
    else:
        if target in source:
            return True
        else:
            return False

# 判断经纬度
def checkLLrange(N, E, S, W, source, include_known = False):
    if source == '-':
        return include_known
    else:
        left, right = source.split(';')
        if '~' in left and '~' in right:
            left_left, left_right = left.split('~')
            left_left_number, left_left_flag = left_left.split(' ')
            left_right_number, left_right_flag = left_right.split(' ')
            if left_left_flag == 'W' and left_right_flag == 'W':
                left_left_number = -float(left_left_number)
                left_right_number = -float(left_right_number)
                if not (W <= left_left_number and left_right_number <= E):
                    return False
            if left_left_flag == 'W' and left_right_flag == 'E':
                left_left_number = -float(left_left_number)
                left_right_number = float(left_right_number)
                if not (W <= left_left_number and left_right_number <= E):
                    return False
            if left_left_flag == 'E' and left_right_flag == 'E':
                left_left_number = float(left_left_number)
                left_right_number = float(left_right_number)
                if not (W <= left_left_number and left_right_number <= E):
                    return False
            
            right_left, right_right = right.split('~')
            right_left_number, right_left_flag = right_left.split(' ')
            right_right_number, right_right_flag = right_right.split(' ')
            if right_left_flag == 'S' and right_right_flag == 'S':
                right_left_number = -float(right_left_number)
                right_right_number = -float(right_right_number)
                if not (S <= right_left_number and right_right_number <= N):
                    return False
            if right_left_flag == 'S' and right_right_flag == 'N':
                right_left_number = -float(right_left_number)
                right_right_number = float(right_right_number)
                if not (S <= right_left_number and right_right_number <= N):
                    return False
            if right_left_flag == 'N' and right_right_flag == 'N':
                right_left_number = float(right_left_number)
                right_right_number = float(right_right_number)
                if not (S <= right_left_number and right_right_number <= N):
                    return False
            return True
        else:
            left_number, left_flag = left.split(' ')
            if left_flag == 'W':
                left_number = -float(left_number)
            if left_flag == 'E':
                left_number = float(left_number)
            if not (W <= left_number and left_number <= E):
                return False
            
            right_number, right_flag = right.split(' ')
            if right_flag == 'S':
                right_number = -float(right_number)
            if right_flag == 'N':
                right_number = float(right_number)
            if not (S <= right_number and right_number <= N):
                return False
            return True

# 综合查询
def read_srp_searched_project_Data(search_data):
    
    bio_project_deduplicated_info = list(settings.SRP_INFO_WITH_DEPTH_AND_LONGITUDE_AND_LATITUDE)

    header = list(bio_project_deduplicated_info[0].keys())

    meta = []

    for item in bio_project_deduplicated_info:

        if not checkSingleField(search_data['srastudyText'], item['SRAStudy']):
            continue
        
        if not checkSingleField(search_data['bioProjectText'], item['BioProject']):
            continue

        if not checkSingleField(search_data['projectID'], item['ProjectID']):
            continue

        if not checkSingleField(search_data['centerName'], item['CenterName']):
            continue

        if not checkSingleField(search_data['submission'], item['Submission']):
            continue

        if not checkSingleField(search_data['genes'], item['genes']):
            continue

        if not checkSingleField(search_data['vfs'], item['vfs']):
            continue

        if not checkSingleField(search_data['args'], item['args']):
            continue

        if not checkSingleField(search_data['taxonome'], item['taxonome']):
            continue

        if not checkSingleField(search_data['product'], item['product']):
            continue

        if not check_depth(item['Depth range'], float(search_data['lowDepth']), float(search_data['highDepth']), search_data['includeUnknownDepth']):
            continue

        if not checkLLrange(float(search_data['n']), float(search_data['e']), float(search_data['s']), float(search_data['w']), item['Longitude and latitude range'], search_data['includeUnknownll']):
            continue

        
        meta.append(item)

    result = {
        'data': meta,
        'header': header,
        'total': len(meta)
    }
    
    return result