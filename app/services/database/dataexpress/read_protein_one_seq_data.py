import os
from Bio import SeqIO
from django.conf import settings

def read_protein_one_seq_data(srp, code):

    contigs_path = os.path.join(settings.DATABASE_PATH, srp, 'annotation', srp + '.faa')
    sequences = SeqIO.parse(contigs_path, 'fasta')

    data = None

    for sequence in sequences:
        if sequence.id == srp + '_' + code:
            data = {
                'ID': sequence.id,
                'Name': sequence.name,
                'Description': sequence.description,
                'Length': len(sequence.seq),
                'Sequence': str(sequence.seq)
            }
    
    result = {
        'data': data
    }

    return result