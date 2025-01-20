import os
import io
import zipfile
import tempfile
from django.http import FileResponse

class ZipUtils:
    def __init__(self):
        pass
    
    @staticmethod
    def zip_file(file_path, zip_name):
        with zipfile.ZipFile(zip_name, 'w') as zf:
            zf.write(file_path, os.path.basename(file_path))
        return open(zip_name, 'rb')

    @staticmethod
    def zip_directory(directory_path, zip_name):
        with zipfile.ZipFile(zip_name, 'w') as zf:
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    zf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), directory_path))
        return open(zip_name, 'rb')

    @staticmethod
    def zip_multiple_items(items, zip_name):
        memory_file = io.BytesIO()
        memory_file.name = zip_name
        with zipfile.ZipFile(memory_file, 'w') as zf:
            for item in items:
                if os.path.isfile(item):
                    zf.write(item, os.path.basename(item))
                elif os.path.isdir(item):
                    for root, dirs, files in os.walk(item):
                        for file in files:
                            zf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), item))
        memory_file.seek(0)
        return memory_file
    

# z = ZipUtils()
# items = [
#     '/home/bioinformatics/projects/dsm/database/SRP121432/annotation',
#     '/home/bioinformatics/projects/dsm/database/test/bio_project_deduplicated_info.csv',
#     '/home/bioinformatics/projects/dsm/database/test/'
# ]
# return z.zip_multiple_items(items, 'asas.zip')