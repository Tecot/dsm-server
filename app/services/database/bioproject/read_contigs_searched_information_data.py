import os
from Bio import SeqIO
from Bio.SeqUtils import GC
from django.conf import settings

def read_contigs_searched_information_data(search_data):
    contigs_path = os.path.join(settings.DATABASE_PATH, search_data['srp'], settings.SRP_GENEOME_SEQ_FILE)
    sequences = SeqIO.parse(contigs_path, 'fasta')
        
    contigs = []
    for seq_record in sequences:
        contigs.append({
            'ID': seq_record.id,
            'Name': search_data['srp'] + '_' + seq_record.name,
            'Description': seq_record.description,
            'GC': round(GC(seq_record.seq), 3), 
            'Sequence': str(seq_record.seq),
            'Length': len(str(seq_record.seq))
        })

    data = []
    for contig in contigs:
        if not checkSingleField(search_data['id'], contig['ID']):
            continue

        if not checkSingleField(search_data['name'], contig['Name']):
            continue

        if not checkSingleField(search_data['description'], contig['Description']):
            continue

        if not checkRangField(float(str(search_data['lengthLow'])), float(str(search_data['lengthHigh'])), contig['Length']):
            continue

        if not checkRangField(float(str(search_data['gcLow'])), float(str(search_data['gcHigh'])), contig['GC']):
            continue

        data.append(contig)
    
    total = len(data)

    header = list(contigs[0].keys())

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
    if target in source:
        return True
    else:
        return False
    
def checkRangField(low_value, hight_value, source):
    if low_value <= source and source <= hight_value:
        return True
    return False