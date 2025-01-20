from django.conf import settings

def read_download_list_data(current_page, page_size):
    
    bio_project_deduplicated_info = list(settings.SRP_INFO_WITH_DEPTH_AND_LONGITUDE_AND_LATITUDE)

    total = len(bio_project_deduplicated_info)

    # header = list(bio_project_deduplicated_info[0].keys())

    slice_data = []

    if total - page_size * current_page > page_size:
        slice_data = bio_project_deduplicated_info[page_size * (current_page - 1) : page_size * current_page]
    else:
        slice_data = bio_project_deduplicated_info[page_size * (current_page - 1) : total]
    
    result = {
        # 'header': header,
        'data': slice_data,
        'total': total
    }

    return result