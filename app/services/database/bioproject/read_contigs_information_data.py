import os
from Bio import SeqIO
from Bio.SeqUtils import GC
from django.conf import settings

def read_contigs_information_data(srp, current_page, page_size):

    contigs_path = os.path.join(settings.DATABASE_PATH, srp, settings.SRP_GENEOME_SEQ_FILE)
    sequences = SeqIO.parse(contigs_path, 'fasta')
    total = len(list(SeqIO.parse(contigs_path, 'fasta')))
        
    contigs = []
    count = 0
    if total > page_size * current_page:
        for seq_record in sequences:
            if count >= page_size * (current_page - 1) and count < page_size * current_page:
                contigs.append({
                    'ID': seq_record.id,
                    'Name': srp + '_' + seq_record.name,
                    'Description': seq_record.description,
                    'GC': round(GC(seq_record.seq), 3), 
                    'Sequence': str(seq_record.seq),
                    'Length': len(str(seq_record.seq))
                })
            count += 1
    else:
        for seq_record in sequences:
            if count >= page_size * (current_page - 1) and count < total:
                contigs.append({
                    'ID': seq_record.id,
                    'Name': srp + '_' + seq_record.name,
                    'Description': seq_record.description,
                    'GC': round(GC(seq_record.seq), 3), 
                    'Sequence': str(seq_record.seq),
                    'Length': len(str(seq_record.seq))
                })
            count += 1

    header = [
        'Id', 
        'Name', 
        'Description', 
        'Length', 
        'GC', 
        'Sequence'
    ] 

    result = {
        'header': header,
        'data': contigs,
        'total': total
    }

    return result