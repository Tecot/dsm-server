'''
File name: 
Author: Tecot (tyx_cqbs@163.com)
Version: V1.0
Date: 2024-12-19 11:31:07
Description: 
'''
import csv
import sys

csv.field_size_limit(sys.maxsize)

def read_csv_as_objects(csv_path):
    objects = []
    with open(csv_path, encoding='utf-8', mode='r', errors='ignore') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            objects.append(row)
            
    return objects