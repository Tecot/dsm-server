import os
import csv
import pandas as pd
from Bio import SeqIO
from Bio.SeqUtils import GC

'''Install
pip:
pip install biopython=1.78
pip install pandas

conda:
conda install biopython=1.78
conda install pandas
'''

'''Run
1、运行单个SRP的数据合并, 代码如下:
    results = combin_data(srp)
    save_csv('SRP121432', results)
2、针对database下所有的srp文件夹合并数据, 每一份合并数据保存在各自的srp文件夹下
    dir_names = [folder for folder in os.listdir(DATABASE_PATH) if os.path.isdir(os.path.join(DATABASE_PATH, folder))]
    srps = [dir_name for dir_name in dir_names if dir_name.startswith('SRP')]  
    for srp in srps:
    results = combin_data(srp)
    save_csv('SRP121432', results)
'''



'''变量配置项'''
# 可变修改项：数据库路径
DATABASE_PATH = '/home/tecot/projects/dsm/database'
# 可变修改项：Contigs文件名
CONTIGS_FILE_NAME = 'final.contigs.fa'
# 可变修改项：vfdb文件名
VFDB_FILE_NAME = 'vfdb.tab'
# 可变修改项：resfinder文件名
RESFINDER_FILE_NAME = 'resfinder.tab'
# 可变修改项：METAWRAP_50_10_BINS文件名
METAWRAP_50_10_BINS_FILE_NAME = 'metawrap_50_10_bins.contigs'
# 可变修改项：GTDBTK_BAC120_SUMMARY文件名
GTDBTK_BAC120_SUMMARY_FILE_NAME = 'gtdbtk.summary.tsv'
# 可变修改项：macrel.out.prediction文件名
MACREL_OUT_PREDICTION = 'macrel.out.prediction'



'''读取srp项目下的contigs文件'''
'''
Output:
[{'id': 'k141_37439', 'name': 'SRP121432_k141_37439', 'length': 552, 'gc': 63.225}, ...]
'''
def read_contigs(srp):
    contigs_file_path = os.path.join(DATABASE_PATH, srp, CONTIGS_FILE_NAME)
    sequences = SeqIO.parse(contigs_file_path, 'fasta')
    results = []
    for seq_record in sequences:
        id = seq_record.id
        name = srp + '_' + seq_record.id
        description = seq_record.description
        length = len(seq_record.seq)
        gc = round(GC(seq_record.seq), 3)
        results.append({
            'id': id,
            'name': name,
            'description': description,
            'length': length,
            'gc': gc,
            'sequence': str(seq_record.seq)
        })
    return results




'''读取srp项目下的vfdb文件'''
'''
Output:
[{'qseqid': 'k141_46824', 'stitle': '(rpoN) RNA polymerase factor sigma-54 [Type IV pili (VF0082) - Adherence (VFC0001)] [Pseudomonas aeruginosa PAO1]'}, ...]
'''
def read_vfdb(srp):
    contigs_file_path = os.path.join(DATABASE_PATH, srp, VFDB_FILE_NAME)
    results = []
    with open(contigs_file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            results.append({
                'qseqid': row[0],
                'stitle': row[12]
            })
    return results




'''读取srp项目下的resfinder文件'''
'''
Output:
[{'qseqid': 'k141_14530', 'sseqid': 'tet(A)_6_AF534183'}, ...]
'''
def read_resfinder(srp):
    contigs_file_path = os.path.join(DATABASE_PATH, srp, RESFINDER_FILE_NAME)
    results = []
    with open(contigs_file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            results.append({
                'qseqid': row[0],
                'sseqid': row[1],
            })
    return results




'''读取srp项目下的gbk文件'''
'''
Output:
{ 'k141_37439': 'msrB_1, ...}
这里利用key   value键值来读取, 目的是提高访问速度, 避免for in循环
'''
def read_gbk(srp):
    gbk_path = os.path.join(DATABASE_PATH, srp, srp + '.gbk')
    results = {}
    with open(gbk_path, "r") as handle:
        for record in SeqIO.parse(handle, "genbank"):
            id = record.id
            # name = record.name
            if len(record.features) > 1:
                hg_index = 0
                gene_str = ''
                for feature in record.features[1:]:
                    temp = {}
                    for item in feature.qualifiers:
                        temp[item] = feature.qualifiers[item][0]
                    
                    if 'gene' not in temp:
                        temp['gene'] = 'hypothetical_gene_' + str(hg_index)
                        hg_index = hg_index + 1
                    gene_str = gene_str + temp['gene'] + ';'
                results[id] = gene_str
    return results




'''读取srp项目下的metawrap_50_10_bins.contigs文件'''
'''
Output:
[{'id': 'k141_74943', 'class': 'bin.2'}, ...]
'''
def read_metawrap(srp):
    metawrap_path = os.path.join(DATABASE_PATH, srp, METAWRAP_50_10_BINS_FILE_NAME)
    results = []
    with open(metawrap_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            results.append({
                'id': row[0],
                'class': row[1],
            })
    return results




'''读取srp项目下的gtdbtk.bac120.summary.tsv文件'''
'''
Output:
[{'id': 'bin.1', 'classification': 's__Thalassolituus oleivorans'}, ...]
'''
def read_gtdbtk(srp):
    gtdbtk_path = os.path.join(DATABASE_PATH, srp, GTDBTK_BAC120_SUMMARY_FILE_NAME)
    results = []
    with open(gtdbtk_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        index = 0
        for row in reader:
            if index != 0:
                results.append({
                    'id': row[0],
                    'classification': row[1].split(';')[len(row[1].split(';')) - 1],
                })
            index = index + 1
    return results



'''读取srp/macrel.out.prediction'''
'''
Output:
{ 'id': id, 'name': name, 'product': 'xxx' }
这个结果知只针对一个region_xx.gbk文件中的数据
'''
def read_amp(srp):
    macrel_out_prediction_path = os.path.join(DATABASE_PATH, srp, MACREL_OUT_PREDICTION)
    results = []
    if os.path.exists(macrel_out_prediction_path):
        with open(macrel_out_prediction_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter='\t')
            for row in reader:
                results.append({
                    'id': row[0],
                    'class': row[1],
                })
    return results


'''读取srp/regions下的gbk文件'''
'''
Output:
{ 'id': id, 'name': name, 'product': 'xxx' }
这个结果知只针对一个region_xx.gbk文件中的数据
'''
def read_region_gbk(srp, contig_id):
    results = {}
    if os.path.exists(os.path.join(DATABASE_PATH, srp, 'regions', contig_id + '.region001.gbk')):
        region_gbk = os.path.join(DATABASE_PATH, srp, 'regions', contig_id + '.region001.gbk')
        with open(region_gbk, "r") as handle:
            for record in SeqIO.parse(handle, "genbank"):
                id = record.id
                name = record.name
                for feature in record.features:
                    if feature.type == 'proto_core':
                        if 'product' in feature.qualifiers:
                            results = {
                                'id': id,
                                'name': name,
                                'product': feature.qualifiers.get('product', '')[0]
                            }
                        else:
                            results = {
                                'id': id,
                                'name': name,
                                'product': '-'
                            }
    else:
        results = {
            'id': contig_id,
            'name': contig_id,
            'product': '-'
        }
    return results

# 读取每个srp项目中macrel.out.predictio中的amps_family数据
def read_amps(srp):
    amps = []
    amps_apth = os.path.join(DATABASE_PATH, srp, 'macrel.out.prediction')
    if os.path.exists(amps_apth):
        with open(amps_apth, 'r') as file:
            content_str = file.read()
            contents = content_str.split('\n')
            headers = contents[0].split('\t')
            data = contents[1:]
            for item_str in data:
                items = item_str.split('\t')
                if items[0] != '':
                    obj = {}
                    for i in range(0, len(headers)):
                        obj[headers[i]] = items[i]
                    amps.append(obj['AMP_family'])
    if len(amps) == 0:
        results = '-'
    else:
        results = ';'.join(list(set(amps)))
    return results

'''合并一个srp中所有需要合并的数据'''
'''
Output:
[
    {
        'id': xxx,
        'name': xxx,
        'length': xxx,
        'gc': xxx,
        'stitle': xxx,
        'sseqid': xxx,
        'genes': xxx,
        'bin': xxx,
        'classification': xxx, 
        'product': xxx
    },
    ...
]
这是一个SRP需要合并的所有数据列表
'''
def combin_data(srp):
    # 创建对象
    results = []
    # 读取各文件中的数据
    contigs = read_contigs(srp)
    vfdbs = read_vfdb(srp)
    resfinders = read_resfinder(srp)
    gbks = read_gbk(srp)
    metawraps = read_metawrap(srp)
    gtdbtks = read_gtdbtk(srp)
    amps = read_amps(srp)
    
    # 装入contig信息
    for contig in contigs:
        # 载入vfdb
        vfdb_stitle = '-'
        for vfdb in vfdbs:
            if contig['id'] == vfdb['qseqid']:
                vfdb_stitle = vfdb_stitle + vfdb['stitle']
                
        # 载入resfinder
        resfinder_sseqid = '-'
        for resfinder in resfinders:
            if contig['id'] == resfinder['qseqid']:
                resfinder_sseqid = resfinder['sseqid']

        # 载入gbks
        genes = '-'
        if contig['id'] in gbks:
            genes = gbks[contig['id']]

        # 载入metawrap_50_10_bins.contigs
        bin = '-'
        for metawrap in metawraps:
            if contig['id'] == metawrap['id']:
                bin = metawrap['class']

        # 载入gtdbtk.bac120.summary
        classification = '-'
        for gtdbtk in gtdbtks:
            if bin == gtdbtk['id']:
                classification = gtdbtk['classification']
                break

        # 载入region
        region = read_region_gbk(srp, contig['id'])
    
        meta = {
            'id': contig['id'],
            'name': contig['name'],
            'description': contig['description'],
            'length': contig['length'],
            'gc': contig['gc'],
            'sequence': contig['sequence'],
            'stitle': vfdb_stitle,
            'sseqid': resfinder_sseqid,
            'genes': genes,
            'bin': bin,
            'classification': classification, 
            'product': region['product'],
            'amps': amps
        }
        # print('Running: [SRP: ' + srp + ']    ' + '[ID: ' + contig['id'] + ']')
        results.append(meta)
    return results




'''将对象列表保存为csv, 该csv保存在每一个srp项目目录下'''
def save_csv(srp, data):
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(DATABASE_PATH, srp, srp + '_combined.csv'), index=False)




'''
1、运行单个SRP的数据合并, 代码如下:
    results = combin_data(srp)
    save_csv('SRP121432', results)
2、针对database下所有的srp文件夹合并数据, 每一份合并数据保存在各自的srp文件夹下
    dir_names = [folder for folder in os.listdir(DATABASE_PATH) if os.path.isdir(os.path.join(DATABASE_PATH, folder))]
    srps = [dir_name for dir_name in dir_names if dir_name.startswith('SRP')]  
    for srp in srps:
    results = combin_data(srp)
    save_csv('SRP121432', results)
'''
if __name__ == '__main__':
    '''case'''
    print('Running start......')
    results = combin_data('SRP121432')
    save_csv('SRP121432', results)
    print('Running stop......')
    # print(read_region_gbk('SRP121432', 'k141_3296'))
    
    
    