import os
import csv
from Bio import SeqIO
from django.conf import settings

def read_cds_vf_resfinder_data(srp, contig_ID):
    csd_data = read_cds_data(srp, contig_ID)
    vfdb_data = read_vfdb_data(srp, contig_ID)
    resfinder_data = read_resfinder_data(srp, contig_ID)
    region_data = read_region_data(srp, contig_ID)
    

    result = {
        'length': csd_data[0],
        'meta': {
            'cdsGenes': csd_data[1],
            'vfGenes': vfdb_data,
            'resfinderGenes': resfinder_data,
            'region': region_data
        }
    }
    return result


# 获取vfdb
def read_vfdb_data(srp, contig_ID):
    vfdb_path = os.path.join(settings.DATABASE_PATH, srp, settings.SRP_VFDB_FILE)
    result = []
    with open(vfdb_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            if row[0] == contig_ID:
                forward = 1
                start = 0
                end = 0
                if int(row[7]) - int(row[6]) < 0:
                    start = int(row[7])
                    end = int(row[6])
                    forward = -1
                else:
                    start = int(row[6])
                    end = int(row[7])
                result.append({
                    'infos': {
                        'qseqid': row[0],
                        'sseqid': row[1],
                        'pident': row[2],
                        'length': row[3],
                        'mismatch': row[4],
                        'gapopen': row[5],
                        'tqstart': row[6],
                        'tqend': row[7],
                        'sstart': row[8],
                        'send': row[9],
                        'evalue': row[10],
                        'bitscore': row[11],
                        'stitle': row[12],
                        'qlen': row[13],
                        'slen': row[14],
                        'qcovs': row[15]
                    },
                    'start': start,
                    'end': end,
                    'gene': row[1].replace('|', '_').replace('(', '_').replace(')', ''),
                    'forward': forward
                })
    return result

# 获取resfinder
def read_resfinder_data(srp, contig_ID):
    resfinder_path = os.path.join(settings.DATABASE_PATH, srp, settings.SRP_RESFINDER_FILE)
    result = []
    with open(resfinder_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            if row[0] == contig_ID:
                forward = 1
                start = 0
                end = 0
                if int(row[7]) - int(row[6]) < 0:
                    start = int(row[7])
                    end = int(row[6])
                    forward = -1
                else:
                    start = int(row[6])
                    end = int(row[7])
                result.append({
                    'infos': {
                        'qseqid': row[0],
                        'sseqid': row[1],
                        'pident': row[2],
                        'length': row[3],
                        'mismatch': row[4],
                        'gapopen': row[5],
                        'tqstart': row[6],
                        'tqend': row[7],
                        'sstart': row[8],
                        'send': row[9],
                        'evalue': row[10],
                        'bitscore': row[11],
                        'stitle': row[12],
                        'qlen': row[13],
                        'slen': row[14],
                        'qcovs': row[15]
                    },
                    'start': start,
                    'end': end,
                    'gene': row[1],
                    'forward': forward
                })
    return result

# 读取GBK cds区
def read_cds_data(srp, contig_ID):
    gbk_path = os.path.join(settings.DATABASE_PATH, srp, srp + '.gbk')
    result = [0, {'meta': []}]
    with open(gbk_path, "r") as handle:
        for record in SeqIO.parse(handle, "genbank"):
            id = record.id
            name = record.name
            description =  record.description
            number_of_features = str(len(record.features))
            sequence = str(record.seq)
            length = record.features[0].location.end

            if record.id == contig_ID:
                meta = []
                if len(record.features) > 1:
                    index = 0
                    for feature in record.features[1:]:
                        qualify_info = {}
                        temp = {}
                        for item in feature.qualifiers:
                            temp[item] = feature.qualifiers[item][0]
                        
                        if 'gene' not in temp:
                            temp['gene'] = 'hypothetical_gene'

                        qualify_info['gene'] = temp['gene']
                        qualify_info['start'] = feature.location.start
                        qualify_info['end'] = feature.location.end
                        qualify_info['forward'] = feature.location.strand
                        qualify_info['info'] = {
                            'id': id,
                            'name': name,
                            'description': description,
                            'number of features': number_of_features,
                            'sequences': sequence,
                        }

                        meta.append(qualify_info)

                        index = index + 1

                result = [length, meta]
                break
    return result

def read_region_data(srp, contig_ID):
    region_path = os.path.join(settings.DATABASE_PATH, srp, 'regions', contig_ID + '.region001.gbk')
    result = []
    if os.path.exists(region_path):
        with open(region_path, "r") as handle:
            for record in SeqIO.parse(handle, "genbank"):
                id = record.id
                name = record.name
                description =  record.description
                number_of_features = str(len(record.features))
                sequence = str(record.seq)
                for feature in record.features:
                    if feature.type == 'protocluster':
                        meta = {
                            'gene': 'protocluster',
                            'start': feature.location.start,
                            'end': feature.location.end,
                            'infos': {
                                'id': id,
                                'name': name,
                                'description': description,
                                'number of features': number_of_features,
                                'sequence': sequence,
                                'category': feature.qualifiers['category'][0],
                                'product': feature.qualifiers['product'][0]
                            }
                        }
                        result.append(meta)
                    if feature.type == 'proto_core':
                        meta = {
                            'gene': 'proto_core',
                            'start': feature.location.start,
                            'end': feature.location.end,
                            'infos': {
                                'id': id,
                                'name': name,
                                'description': description,
                                'number of features': number_of_features,
                                'sequence': sequence,
                                'product': feature.qualifiers['product'][0]
                            }
                        }
                        result.append(meta)
    return result






# def read_geneome_contig_gbk_data(srp, contig_ID):
#     gbk_path = os.path.join(settings.DATABASE_PATH, srp, srp + '.gbk')
#     result = {}
#     with open(gbk_path, "r") as handle:
#         for record in SeqIO.parse(handle, "genbank"):
#             if record.id == contig_ID:
#                 # 基础信息
#                 # print('基础信息：')
#                 # print('ID:' + record.id)
#                 # print('Name:' + record.name)
#                 # print('Description:' + record.description)
#                 # print('Number of features:' + str(len(record.features)))
#                 # print('Record annotations:' + str(record.annotations))
#                 # print('Sequence:' + record.seq)
#                 id = record.id
#                 name = record.name
#                 description =  record.description
#                 number_of_features = str(len(record.features))
#                 record_annotations = str(record.annotations)
#                 sequence = str(record.seq)

#                 meta = []
#                 length = record.features[0].location.end
                
#                 if len(record.features) > 1:
#                     index = 0
#                     for feature in record.features[1:]:
#                         qualify_info = {}
#                         for item in feature.qualifiers:
#                             qualify_info[item] = feature.qualifiers[item][0]
                        
#                         if 'gene' not in qualify_info:
#                             qualify_info['gene'] = 'hypothetical_gene_' + str(index)

#                         qualify_info['start'] = feature.location.start
#                         qualify_info['end'] = feature.location.end
#                         qualify_info['forward'] = feature.location.strand

#                         meta.append(qualify_info)

#                         index = index + 1

#                 result = {
#                     'id': id,
#                     'name': name,
#                     'description': description,
#                     'number of features': number_of_features,
#                     'record annotations': record_annotations,
#                     'sequences': sequence,
#                     'length': length,
#                     'meta': meta
#                 }

#                 break
    
#     return result