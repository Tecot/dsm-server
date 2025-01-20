'''
File name: 
Author: Tecot (tyx_cqbs@163.com)
Version: V1.0
Date: 2024-09-02 16:57:16
Description: 
'''
import os
import csv
import pandas as pd
# from app.utils.read_csv_as_objects import read_csv_as_objects

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

# 修改这个路径
DATABASE_PATH = '/home/tecot/projects/dsm/database'

def combined_srp_project():
    srps = [d for d in os.listdir(DATABASE_PATH) if os.path.isdir(os.path.join(DATABASE_PATH, d))]
    bio_project_info = read_csv_as_objects(os.path.join(DATABASE_PATH, 'bio_project_info.csv'))
    data = []
    for srp in srps:
        obj = {}
        for bio_project in bio_project_info:
            if bio_project['SRAStudy'] == srp:
                obj = bio_project
                break
        srps_combined_data = read_csv_as_objects(os.path.join(DATABASE_PATH, srp, srp + '_combined.csv'))
        
        
        genes = []
        stitle = []
        sseqid = []
        classification = []
        product = []
        amps = []

        for cd in srps_combined_data:
            # 提取基因
            if cd['genes'] != '-':
                current_genes = cd['genes'].split(';')
                for gene in current_genes:
                    genes.append(gene.split('_')[0])
            # 提取Stitle
            if cd['stitle'] != '-':
                stitle.append(cd['stitle'].split(' ')[0].replace('(', '').replace(')','').replace('-',''))
            # 提取Sseqid
            if cd['sseqid'] != '-':
                sseqid.append(cd['sseqid'])
            # 提取classification
            if cd['classification'] != '-' and cd['classification'] != 's__':
                classification.append(cd['classification'])
            # 提取Product
            if cd['product'] != '-':
                product.append(cd['product'])
            # 提取amps
            if cd['amps'] != '-':
                amps.append(cd['amps'])
        new_genes = ';'.join(list(set(genes)))
        this_genes = ''
        if new_genes[0] == ';':
            this_genes = new_genes[1:]
        else:
            this_genes = new_genes
        this_stitle = ';'.join(list(set(stitle)))
        this_sseqid = ';'.join(list(set(sseqid)))
        this_classification = ';'.join(list(set(classification)))
        this_product = ';'.join(list(set(product)))
        this_amps = ';'.join(list(set(amps)))
        obj['genes'] = this_genes
        obj['vfs'] = this_stitle
        obj['args'] = this_sseqid
        obj['taxonome'] = this_classification
        obj['product'] = this_product
        obj['amps'] = this_amps
        data.append(obj)
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(DATABASE_PATH, 'bio_project_deduplicated_info.csv'), index=False)    


if __name__ == '__main__':
    combined_srp_project()