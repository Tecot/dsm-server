from django.conf import settings

def read_srp_project_Data(current_page, page_size):
    bio_project_deduplicated_info = list(settings.SRP_INFO_WITH_DEPTH_AND_LONGITUDE_AND_LATITUDE)

    total = len(bio_project_deduplicated_info)

    header = list(bio_project_deduplicated_info[0].keys())

    slice_data = []

    if total - page_size * current_page > page_size:
        slice_data = bio_project_deduplicated_info[page_size * (current_page - 1) : page_size * current_page]
    else:
        slice_data = bio_project_deduplicated_info[page_size * (current_page - 1) : total]
    
    result = {
        'header': header,
        'data': slice_data,
        'total': total
    }

    return result




    # df = pd.read_csv(os.path.join(settings.DATABASE_PATH, settings.BIO_PROJECT_DEDUPLICATED_INFO), encoding='utf8', encoding_errors='ignore')

    # total = len(df[0:])
    # header = list(df.columns)
    # csv_data = []

    # if total - page_size * current_page > page_size:
    #     csv_data = df.iloc[page_size * (current_page - 1) : page_size * current_page].to_json(orient='records', force_ascii=False)
    # else:
    #     csv_data = df.iloc[page_size * (current_page - 1) : total].to_json(orient='records', force_ascii=False)
    
    # return_data = {
    #     'header': header,
    #     'data': csv_data,
    #     'tablePageInfo': {
    #         'total': total,
    #         'currentPage': current_page,
    #         'pageSize': page_size
    #     }  
    # }

    # return return_data
