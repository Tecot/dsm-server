from django.conf import settings
from app.utils.read_csv_as_objects import read_csv_as_objects

def read_contig_project_searched_Data(search_data):
    contigs_project_data = read_csv_as_objects(settings.DATABASE_PATH + '/' + search_data['srp'] + '/' + search_data['srp'] + '_combined.csv')
    data = []
    for item in contigs_project_data:
        if not checkSingleField(search_data['name'], item['name']):
            continue

        if not checkSingleField(search_data['id'], item['id']):
            continue

        if not checkSingleField(search_data['description'], item['description']):
            continue

        if not checkRangField(float(str(search_data['lengthLow'])), float(str(search_data['lengthHigh'])), float(str(item['length']))):
            continue

        if not checkRangField(float(str(search_data['gcLow'])), float(str(search_data['gcHigh'])), float(str(item['gc']))):
            continue

        if not checkContainUnknownField(search_data['ifSearchStitleUnknown'], search_data['stitle'], item['stitle']):
            continue

        if not checkContainUnknownField(search_data['ifSearchSseqidUnknown'], search_data['sseqid'], item['sseqid']):
            continue

        if not checkContainUnknownField(search_data['ifSearchGenesUnknown'], search_data['genes'], item['genes']):
            continue

        if not checkContainUnknownField(search_data['ifSearchBinUnknown'], search_data['bin'], item['bin']):
            continue

        if not checkContainUnknownField(search_data['ifSearchClassificationUnknown'], search_data['classification'], item['classification']):
            continue
        
        if not checkContainUnknownField(search_data['ifSearchProductUnknown'], search_data['product'], item['product']):
            continue

        data.append(item)

    total = len(data)

    header = list(contigs_project_data[0].keys())

    slice_data = []

    page_size = int(str(search_data['pageSize']))
    current_page = int(str(search_data['currentPage']))

    if total - page_size * current_page > page_size:
        slice_data = data[page_size * (current_page - 1) : page_size * current_page]
    else:
        slice_data = data[page_size * (current_page - 1) : total]
    
    result = {
        'header': header,
        'data': slice_data,
        'total': total
    }

    return result

def checkSingleField(target, source):
    if target == '-':
        return False
    else:
        if target in source:
            return True
        else:
            return False
        
def checkRangField(low_value, hight_value, source):
    if low_value <= source and source <= hight_value:
        return True
    return False

def checkContainUnknownField(isContainerUnknown, target, source):
    if isContainerUnknown == 'false':
        if target in source:
            return True
        else:
            return False
    else:
        if source == '-':
            return True
        else:
            return False     
