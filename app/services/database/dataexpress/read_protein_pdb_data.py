import os
from django.conf import settings

def read_protein_pdb_data(srp, code):
    pdb_path = os.path.join(settings.DATABASE_PATH, srp, 'pro_str', srp + '_' + code + '.pdb')
    result = {}
    if os.path.exists(pdb_path):
        with open(pdb_path, 'r') as file:
            pdb_str = file.read()
        
        result = {
            'data': pdb_str
        }
    else:
        result = {
            'data': None
        }

    return result