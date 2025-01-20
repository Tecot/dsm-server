import os
from Bio import SeqIO
from Bio.SeqUtils import GC
from django.conf import settings

def read_protein_seq_data(srp):
    data = []
    
    contigs_path = os.path.join(settings.DATABASE_PATH, srp, 'annotation', srp + '.faa')
    sequences = SeqIO.parse(contigs_path, 'fasta')

    for seq_record in sequences:
        data.append({
            'ID': seq_record.id,
            'Name': seq_record.name,
            'Description': seq_record.description,
            'Length': len(seq_record.seq),
            'Sequence': str(seq_record.seq)
        })
            
    header = [
        'ID',
        'Name',
        'Description',
        'Length',
        'Sequence'
    ]
        
    
    result = {
        'header': header,
        'data': data,
        'total': len(data)
    }

    return result