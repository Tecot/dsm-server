import os
import csv
from django.conf import settings

def read_bin_data(srp):
    gtdb_bac120_data = read_gtdb_bac120_data(srp)
    metawrap_50_10_bins_data = read_metawrap_50_10_bins_data(srp)
    data = []
    for metawrap_item in metawrap_50_10_bins_data:
        bin = metawrap_item['bin']
        completeness = metawrap_item['completeness']
        contamination = metawrap_item['contamination']
        gc = metawrap_item['GC']
        n50 = metawrap_item['N50']
        size = metawrap_item['size']
        for gtdb_item in gtdb_bac120_data:
            if bin == gtdb_item['user_genome']:
                fastani_reference = gtdb_item['fastani_reference']
                fastani_ani = gtdb_item['fastani_ani']
                fastani_af = gtdb_item['fastani_af']
                closest_placement_reference = gtdb_item['closest_placement_reference']
                closest_placement_ani = gtdb_item['closest_placement_ani']
                closest_placement_af = gtdb_item['closest_placement_af']
                msa_percent = gtdb_item['msa_percent']
                classificationes = gtdb_item['classification'].split(';')
                domain = classificationes[0].split('__')[1]
                phylum = classificationes[1].split('__')[1]
                class0 = classificationes[2].split('__')[1]
                order = classificationes[3].split('__')[1]
                family = classificationes[4].split('__')[1]
                genus = classificationes[5].split('__')[1]
                species = classificationes[6].split('__')[1]
                data.append({
                    'bin': bin,
                    'domain': domain,
                    'phylum': phylum,
                    'class': class0,
                    'order': order,
                    'family': family,
                    'genus': genus,
                    'species': species,
                    'completeness': completeness,
                    'contamination': contamination,
                    'gc': gc,
                    'n50': n50,
                    'size': size,
                    'fastaniReference': fastani_reference,
                    'fastaniAni': fastani_ani,
                    'fastaniAf': fastani_af,
                    'closestPlacementReference': closest_placement_reference,
                    'closestPlacementAni': closest_placement_ani,
                    'closestPlacementAf': closest_placement_af,
                    'msaPercent': msa_percent
                })
                continue
    
    result = {
        'data': data
    }

    return result

def read_metawrap_50_10_bins_data(srp):
    metawrap_50_10_bins_path = os.path.join(settings.DATABASE_PATH, srp, settings.METAWRAP_50_10_BINS_FILE)
    result = []
    headers = []
    index = 0
    with open(metawrap_50_10_bins_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            if index == 0:
                headers = row
                index = index + 1
            else:
                temp = {}
                pos = 0
                for item in row:
                    temp[headers[pos]] = item
                    pos = pos + 1
                result.append(temp)
    
    return result

def read_gtdb_bac120_data(srp):
    gtdb_bac120_path = os.path.join(settings.DATABASE_PATH, srp, settings.GTDBTK_BAC120_SUMMARY_FILE)
    result = []
    headers = []
    index = 0
    with open(gtdb_bac120_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            if index == 0:
                headers = row
                index = index + 1
            else:
                temp = {}
                pos = 0
                for item in row:
                    temp[headers[pos]] = item
                    pos = pos + 1
                result.append(temp)
    
    return result
