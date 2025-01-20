from django.conf import settings
from app.utils.read_csv_as_objects import read_csv_as_objects

def read_contig_project_Data(srp, current_page, page_size):
    srps_combined_data = read_csv_as_objects(settings.DATABASE_PATH + '/' + srp + '/' + srp + '_combined.csv')
    
    total = len(srps_combined_data)

    header = list(srps_combined_data[0].keys())

    slice_data = []

    if total - page_size * current_page > page_size:
        slice_data = srps_combined_data[page_size * (current_page - 1) : page_size * current_page]
    else:
        slice_data = srps_combined_data[page_size * (current_page - 1) : total]
    
    result = {
        'header': header,
        'data': slice_data,
        'total': total
    }
    
    return result



    # ================YES
    # bio_project_deduplicated_info = list(settings.SRP_DEDUPLICATED_INFO)
    # contigs_total = len(bio_project_deduplicated_info)

    # data = []
    # for item in bio_project_deduplicated_info:
    #     contigs_path = os.path.join(settings.DATABASE_PATH, item['SRPStudy'], settings.SRP_CONTIGS_FILE)
    #     sequences = SeqIO.parse(contigs_path, 'fasta')

    #     contig_total = 0
    #     length_list = []
    #     GC_content_list = []
    #     for seq_record in sequences:
    #         length = len(seq_record.seq)
    #         GC_content = round(GC(seq_record.seq), 3)
    #         length_list.append(length)
    #         GC_content_list.append(GC_content)
    #         contig_total += 1
    #     max_length = max(length_list)
    #     min_length = min(length_list)
    #     max_GC_content = max(GC_content_list)
    #     min_GC_content = min(GC_content_list)
    #     data.append({
    #         'Contigs name': test + '_' + 'contigs',
    #         'Max length': max_length,
    #         'Min length': min_length,
    #         'Max GC conetnt': max_GC_content,
    #         'Min GC content': min_GC_content,
    #         'Contig total': contig_total,
    #     })
        
    # header = [
    #     'Contigs name', 
    #     'Max length',
    #     'Min length',
    #     'Max GC conetnt',
    #     'Min GC content',
    #     'Contig total'
    # ]
        
    
    # result = {
    #     'header': header,
    #     'data': data,
    #     'contigsTotal': contigs_total
    # }

    # return result