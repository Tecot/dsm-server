import os
from django.conf import settings

def read_srp_dir_names_data():
    sub_dirs = [d for d in os.listdir(settings.DATABASE_PATH) if os.path.isdir(os.path.join(settings.DATABASE_PATH, d))]
    
    result = {
        'data': sub_dirs
    }

    return result


