# from django.test import TestCase
# import os
# from Bio import SeqIO, SeqFeature
# from Bio.SeqFeature import FeatureLocation
# import collections

# path = '/home/bioinformatics/projects/dsm/database/SRP121432/SRP121432.gbk'
# contig_ID = 'k141_37439'


# import os
# import csv


# def read_macrel_out_prediction_data():
#     with open('/home/tecot/projects/dsm/database/SRP121432/macrel.out.prediction', 'r') as file:
#         content_str = file.read()
#         contents = content_str.split('\n')
#         headers = contents[0].split('\t')
#         data = contents[1:]
#         dicts = []
#         for item_str in data:
#             items = item_str.split('\t')
#             if items[0] != '':
#                 obj = {}
#                 for i in range(0, len(headers)):
#                     obj[headers[i]] = items[i]
#                 dicts.append(obj)
#         print(dicts[1:2])

# read_macrel_out_prediction_data()



# def read_region_data(srp, contig_ID):
#     region_path = os.path.join('/home/bioinformatics/projects/dsm/database', srp, 'regions', contig_ID + '.region001.gbk')
#     result = []
#     if os.path.exists(region_path):
#         with open(region_path, "r") as handle:
#             for record in SeqIO.parse(handle, "genbank"):
#                 id = record.id
#                 name = record.name
#                 description =  record.description
#                 number_of_features = str(len(record.features))
#                 sequence = str(record.seq)
#                 for feature in record.features:
#                     if feature.type == 'protocluster':
#                         meta = {
#                             'gene': 'protocluster',
#                             'start': feature.location.start,
#                             'end': feature.location.end,
#                             'infos': {
#                                 'id': id,
#                                 'name': name,
#                                 'description': description,
#                                 'number of features': number_of_features,
#                                 'sequence': sequence,
#                                 'category': feature.qualifiers['category'][0],
#                                 'product': feature.qualifiers['product'][0]
#                             }
#                         }
#                         result.append(meta)
#                     if feature.type == 'proto_core':
#                         meta = {
#                             'gene': 'proto_core',
#                             'start': feature.location.start,
#                             'end': feature.location.end,
#                             'infos': {
#                                 'id': id,
#                                 'name': name,
#                                 'description': description,
#                                 'number of features': number_of_features,
#                                 'sequence': sequence,
#                                 'product': feature.qualifiers['product'][0]
#                             }
#                         }
#                         result.append(meta)
#     print(result)
# read_region_data('SRP121432', 'k141_4145')
# def detail_longitudes_to_range(longitudes):
#     longitudes_range = '-'
#     longitudes_delete_temp_str = [x for x in longitudes if x != '']
#     if len(longitudes_delete_temp_str):
#         if all(item == longitudes_delete_temp_str[0] for item in longitudes_delete_temp_str):
#             longitudes_range = longitudes_delete_temp_str[0]
#         else:
#             max_W_longitude = 9999
#             min_W_longitude = 9999
#             max_E_longitude = 9999
#             min_E_longitude = 9999
#             w_flag = True
#             e_flag = True
#             for item in longitudes_delete_temp_str:
#                 longitude, forward= item.split(' ')

#                 if forward == 'W':
#                     if w_flag:
#                         max_W_longitude = float(longitude)
#                         min_W_longitude = float(longitude)
#                         w_flag = False
#                     else:
#                         if float(longitude) > max_W_longitude:
#                             max_W_longitude = float(longitude)
#                         if float(longitude) < min_W_longitude:
#                             min_W_longitude = float(longitude)
#                 if forward == 'E':
#                     if e_flag:
#                         max_E_longitude = float(longitude)
#                         min_E_longitude = float(longitude)
#                         e_flag = False
#                     else:
#                         if float(longitude) > max_E_longitude:
#                             max_E_longitude = float(longitude)
#                         if float(longitude) < min_E_longitude:
#                             min_E_longitude = float(longitude)
            
#             if max_W_longitude != 9999 and min_W_longitude != 9999 and max_E_longitude != 9999 and min_E_longitude != 9999:
#                 longitudes_range = str(max_W_longitude) + ' W~' + str(max_E_longitude) + ' E'

#             if max_W_longitude != 9999 and min_W_longitude != 9999 and max_E_longitude == 9999 and min_E_longitude == 9999:
#                 if min_W_longitude == max_W_longitude:
#                     longitudes_range = str(max_W_longitude) + ' W'
#                 else:
#                     longitudes_range = str(min_W_longitude) + ' W~' + str(max_W_longitude) + ' W'
            
#             if max_W_longitude == 9999 and min_W_longitude == 9999 and max_E_longitude != 9999 and min_E_longitude != 9999:
#                 if min_E_longitude == max_E_longitude:
#                     longitudes_range = str(max_E_longitude) + ' E'
#                 else:
#                     longitudes_range = str(min_E_longitude) + ' E~' + str(max_E_longitude) + ' E'     
#     return longitudes_range
# print(detail_longitudes_to_range(['0 E', '0 E', '0.001 E', '0.001 E', '2.30265 E', '2.30265 E', '4.5 E', '4.5 E', '6.6 E', '6.6 E', '10.802 E', '10.802 E', '11.8 E', '11.8 E', '13.3 E', '13.3 E', '6.59983 E', '6.59983 E', '8.50038333 E', '8.50038333 E', '13.30187 E', '13.30187 E', '0.00185 E', '0.00185 E', '0.0013 E', '0.0013 E', '0.0019 E', '0.0019 E', '4.4989 E', '4.4989 E']))

# def checkLLrange(N, E, S, W, source):
#     if source == '-':
#         return True
#     else:
#         left, right = source.split(';')
#         if '~' in left and '~' in right:
#             left_left, left_right = left.split('~')
#             left_left_number, left_left_flag = left_left.split(' ')
#             left_right_number, left_right_flag = left_right.split(' ')
#             if left_left_flag == 'W' and left_right_flag == 'W':
#                 left_left_number = -float(left_left_number)
#                 left_right_number = -float(left_right_number)
#                 if not (W <= left_left_number and left_right_number <= E):
#                     return False
#             if left_left_flag == 'W' and left_right_flag == 'E':
#                 left_left_number = -float(left_left_number)
#                 left_right_number = float(left_right_number)
#                 if not (W <= left_left_number and left_right_number <= E):
#                     return False
#             if left_left_flag == 'E' and left_right_flag == 'E':
#                 left_left_number = float(left_left_number)
#                 left_right_number = float(left_right_number)
#                 if not (W <= left_left_number and left_right_number <= E):
#                     return False
            
#             right_left, right_right = right.split('~')
#             right_left_number, right_left_flag = right_left.split(' ')
#             right_right_number, right_right_flag = right_right.split(' ')
#             if right_left_flag == 'S' and right_right_flag == 'S':
#                 right_left_number = -float(right_left_number)
#                 right_right_number = -float(right_right_number)
#                 if not (S <= right_left_number and right_right_number <= N):
#                     return False
#             if right_left_flag == 'S' and right_right_flag == 'N':
#                 right_left_number = -float(right_left_number)
#                 right_right_number = float(right_right_number)
#                 if not (S <= right_left_number and right_right_number <= N):
#                     return False
#             if right_left_flag == 'N' and right_right_flag == 'N':
#                 right_left_number = float(right_left_number)
#                 right_right_number = float(right_right_number)
#                 if not (S <= right_left_number and right_right_number <= N):
#                     return False
#             return True
#         else:
#             left_number, left_flag = left.split(' ')
#             if left_flag == 'W':
#                 left_number = -float(left_number)
#             if left_flag == 'E':
#                 left_number = float(left_number)
#             if not (W <= left_number and left_number <= E):
#                 return False
            
#             right_number, right_flag = right.split(' ')
#             if right_flag == 'S':
#                 right_number = -float(right_number)
#             if right_flag == 'N':
#                 right_number = float(right_number)
#             if not (S <= right_number and right_number <= N):
#                 return False
#             return True


# print(checkLLrange(45, 90, -34, -120, '20 W~45 E;30 S~40 N'))



# def check_depth(depth_range, low_depth, high_depth):
#     new_depth_range = str(depth_range)
#     if new_depth_range == '-':
#             return False
#     else:
#         if '~' in new_depth_range:
#             low_depth_str, high_depth_str = new_depth_range.split('~')
#             float_low_depth = float(low_depth_str)
#             float_high_depth = float(high_depth_str)
#             if not (low_depth <= float_low_depth and float_high_depth <= high_depth):
#                 return False
#         else:
#             float_depth = float(new_depth_range)
#             if not (low_depth <= float_depth and float_depth <= high_depth):
#                 return False
#     return True
        
# print(check_depth(234.22, 0, 6000))


# def read_gtdb_bac120_data():
#     gtdb_bac120_path = '/home/bioinformatics/projects/dsm/database/SRP121432/gtdbtk.bac120.summary.tsv'
#     result = []
#     headers = []
#     index = 0
#     with open(gtdb_bac120_path, 'r', newline='', encoding='utf-8') as file:
#         reader = csv.reader(file, delimiter='\t')
#         for row in reader:
#             if index == 0:
#                 headers = row
#                 index = index + 1
#             else:
#                 temp = {}
#                 pos = 0
#                 for item in row:
#                     temp[headers[pos]] = item
#                     pos = pos + 1
#                 result.append(result)
    # print(result)
            
# read_gtdb_bac120_data()

# def read_cds_data():
#     # gbk_path = os.path.join(settings.DATABASE_PATH, srp, srp + '.gbk')
#     result = {}
#     with open(path, "r") as handle:
#         for record in SeqIO.parse(handle, "genbank"):
#             id = record.id
#             name = record.name
#             description =  record.description
#             number_of_features = str(len(record.features))
#             sequence = str(record.seq)
#             length = record.features[0].location.end
#             # print('-----')
#             # print(id)
#             # print(name)
#             # print(description)
#             # print(number_of_features)
            
#             # print('-----')

#             if record.id == contig_ID:
#                 meta = []
#                 if len(record.features) > 1:
#                     index = 0
#                     for feature in record.features[1:]:
#                         qualify_info = {}
#                         temp = {}
#                         for item in feature.qualifiers:
#                             temp[item] = feature.qualifiers[item][0]
                        
#                         if 'gene' not in temp:
#                             temp['gene'] = 'Hypothetical gene'

#                         qualify_info['gene'] = temp['gene']
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
#                     'sequences': sequence,
#                     'length': length,
#                     'meta': meta
#                 }

#                 break
    # print(result)
    # return result
# read_cds_data()
 
# 读取GenBank文件
# index = 0
# with open(path, "r") as handle:
#     for record in SeqIO.parse(handle, "genbank"):
#         if record.id == contig_ID:
#             for feature in record.features:
#                 print('----')
#                 print(feature)
            # 基础信息
            # print('基础信息：')
            # print('ID:' + record.id)
            # print('Name:' + record.name)
            # print('Description:' + record.description)
            # print('Number of features:' + str(len(record.features)))
            # print('Record annotations:' + str(record.annotations))
            # print('Sequence:' + record.seq)

            # for feature in record.features:
            #     # 获取每个feature的location
            #     location = feature.location
            #     if isinstance(location, FeatureLocation):
            #         start = location.start
            #         end = location.end
            #         strand = location.strand
                
            #     featuresInfo = []
            #     qualifiers = feature.qualifiers
            #     if isinstance(qualifiers, collections.OrderedDict):
            #         dic = {}
            #         for item in qualifiers:
            #             dic[item] = qualifiers[item][0] if len(qualifiers[item]) != 0 else ''
            #         featuresInfo.append(dic)
            #     print(featuresInfo)
            # break
        # for feature in record.features:
        #     # 获取每个feature的location
        #     location = feature.location
            
        #     # 打印方向
        #     if isinstance(location, FeatureLocation):
        #         strand = location.strand
        #         print(f"Feature {feature.type} is on strand: {strand}")



# with open(path, 'r') as handle:
#     records = SeqIO.parse(handle, "genbank")
#     result = {}
#     for record in records:
#         if record.id == contig_ID:
#             features_number = len(record.features)
#             # 基础信息
#             # print('基础信息：')
#             # print('ID:' + record.id)
#             # print('Name:' + record.name)
#             # print('Description:' + record.description)
#             # print('Number of features:' + str(len(record.features)))
#             # print('Record annotations:' + str(record.annotations))
#             # feature[0]
#             print('features[0]信息：')
#             f0 = record.features[0]
#             print('Type: ' + f0.type)
#             print(f0.location.start)
#             print(f0.location.end)
#             print(f0.location.parts)
#             # print(type(f0.location))
#             SeqFeature.FeatureLocation
#             if features_number == 2:
#                 pass
                

#             # print('Type: ' + f0.type)
#             # print('start: ' + f0.location)
#             break
#         else:
#             continue




# 读vfdb

path = '/home/bioinformatics/projects/dsm/database/SRP121432/resfinder.tab'
contig_ID = 'k141_14530'
import csv

# def read_vfdb_data():
#     result = []
#     with open(path, 'r', newline='', encoding='utf-8') as file:
#         reader = csv.reader(file, delimiter='\t')
#         for row in reader:
#             result.append({
#                 'qseqid': row[0],
#                 'sseqid': row[1],
#                 'pident': row[2],
#                 'length': row[3],
#                 'mismatch': row[4],
#                 'gapopen': row[5],
#                 'qstart': row[6],
#                 'qend': row[7],
#                 'sstart': row[8],
#                 'send': row[9],
#                 'evalue': row[10],
#                 'bitscore': row[11],
#                 'stitle': row[12],
#                 'qlen': row[13],
#                 'slen': row[14],
#                 'qcovs': row[15]
#             })
#     print(result)
# def read_vfdb_data():
#     with open(path, 'r') as file:
#         str_content = file.read()
#         str_content_array = str_content.split('\n')
#         for line in str_content_array:
#             print(line.split('\t'))

# read_vfdb_data()