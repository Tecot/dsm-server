#!/bin/bash

# Global configuration
declare -A software_paths
software_paths["bwa"]="/home/tecot/softwares/bwa/bwa"
software_paths["samtools"]="/home/tecot/softwares/samtools/samtools-1.9/samtools"
software_paths["megahit"]="python /home/tecot/softwares/megahit/megahit/build/megahit"
software_paths["seqGraph"]="/home/tecot/softwares/seqGraph"
software_paths["quast"]="/home/tecot/softwares/quast-5.2.0/quast.py"
software_paths["blastn"]="/home/tecot/softwares/blastn/ncbi-blast-2.9.0+/bin/blastn"

software_paths["metawrap"]="metawrap"
software_paths["gtdbtk"]="gtdbtk"
software_paths["antismash"]="antismash"
software_paths["macrel"]="macrel"

declare -A database_paths
database_paths["VFDB"]="/home/tecot/projects/dsm/dsm-server/datasets/VFDB"
database_paths["resfinder"]="/home/tecot/projects/dsm/dsm-server/datasets/resfinder"

declare -A conda_envs
conda_envs["antismash"]="antismash"
conda_envs["metawrap"]="metawrap"
conda_envs["gtdbtk"]="gtdbtk"

# Function to run a command and handle errors
run_command() {
    eval "$1"
    if [ $? -ne 0 ]; then
        echo "An error occurred: $1"
        exit 1
    fi
}

# Function to setup conda environment
setup_environment() {
    current_env=$(conda info --envs | grep '*' | awk '{print $1}')
    if [ "$current_env" != "$1" ]; then
        echo "Activating conda environment: $1"
        source "$(conda info --base)/etc/profile.d/conda.sh"
        conda activate "$1"
    fi
}

# Megahit function
megahit() {
    out_dir=$1
    user=$2
    file=$3
    megahit_cmd="${software_paths['megahit']} -1 ${out_dir}/${user}/${user}_1.fastq -2 ${out_dir}/${user}/${user}_2.fastq -t 28 --min-contig-len 500 --out-dir ${out_dir}/${user}/1.megahit"
    run_command "$megahit_cmd"
    remove_cmd="rm -r ${out_dir}/${user}/1.megahit/intermediate_contigs"
    run_command "$remove_cmd"
}

# SeqGraph function
seqgraph() {
    out_dir=$1
    user=$2
    file=$3
    mkdir -p "${out_dir}/${user}/2.seqgraph"
    bwa_index_cmd="${software_paths['bwa']} index ${file}"
    run_command "$bwa_index_cmd"
    bwa_mem_cmd="${software_paths['bwa']} mem -t 30 ${file} ${out_dir}/${user}/${user}_1.fastq ${out_dir}/${user}/${user}_2.fastq > ${out_dir}/${user}/2.seqgraph/${user}.sam"
    run_command "$bwa_mem_cmd"
    samtools_view_cmd="${software_paths['samtools']} view -Sb ${out_dir}/${user}/2.seqgraph/${user}.sam > ${out_dir}/${user}/2.seqgraph/${user}.bam"
    run_command "$samtools_view_cmd"
    samtools_sort_cmd="${software_paths['samtools']} sort -o ${out_dir}/${user}/2.seqgraph/${user}_sorted.bam ${out_dir}/${user}/2.seqgraph/${user}.bam"
    run_command "$samtools_sort_cmd"
    samtools_index_cmd="${software_paths['samtools']} index ${out_dir}/${user}/2.seqgraph/${user}_sorted.bam"
    run_command "$samtools_index_cmd"
    samtools_depth_cmd="${software_paths['samtools']} depth ${out_dir}/${user}/2.seqgraph/${user}_sorted.bam > ${out_dir}/${user}/2.seqgraph/${user}.depth"
    run_command "$samtools_depth_cmd"
    depth_avg_cmd="${software_paths['depth_aver']} ${out_dir}/${user}/2.seqgraph/${user}.depth"
    number=$(eval "$depth_avg_cmd")
    export LD_LIBRARY_PATH="${software_paths['seqGraph']}/htslib/lib:$LD_LIBRARY_PATH"
    generate_graph_cmd="${software_paths['seqGraph']}/generatesingleGraph ${out_dir}/${user}/2.seqgraph/${user}_sorted.bam ${out_dir}/${user}/2.seqgraph/${user}.graph $number"
    run_command "$generate_graph_cmd"
    matching_cmd="${software_paths['seqGraph']}/build/matching -g ${out_dir}/${user}/2.seqgraph/${user}.graph -r ${out_dir}/${user}/2.seqgraph/${user}.result -c ${out_dir}/${user}/2.seqgraph/${user}.cl --model 1 --verbose 1 -s"
    run_command "$matching_cmd"
    remove_sam_cmd="rm ${out_dir}/${user}/2.seqgraph/${user}.sam"
    run_command "$remove_sam_cmd"
    remove_bam_cmd="rm ${out_dir}/${user}/2.seqgraph/${user}.bam"
    run_command "$remove_bam_cmd"
    remove_sorted_bam_cmd="rm ${out_dir}/${user}/2.seqgraph/${user}_sorted.bam"
    run_command "$remove_sorted_bam_cmd"
    make_fa_cmd="${software_paths['make_fa']} ${out_dir}/${user}/1.megahit/final.contigs.fa ${out_dir}/${user}/2.seqgraph/${user}.result ${out_dir}/${user}/2.seqgraph/${user}_dirty.fa"
    run_command "$make_fa_cmd"
    clean_cmd="${software_paths['clean']} ${out_dir}/${user}/2.seqgraph/${user}_dirty.fa ${out_dir}/${user}/2.seqgraph/${user}.fa"
    run_command "$clean_cmd"
    seqtk_cmd="seqtk seq -L 1000 ${out_dir}/${user}/2.seqgraph/${user}.fa > ${out_dir}/${user}/2.seqgraph/${user}_1000.fa"
    run_command "$seqtk_cmd"
}

# Quast function
quast() {
    out_dir=$1
    user=$2
    file=$3
    setup_environment "${conda_envs['antismash']}"
    quast_cmd="${software_paths['quast']} ${file} -o ${out_dir}/${user}/3.quast -t 20"
    run_command "$quast_cmd"
}

# Bin function
binning() {
    out_dir=$1
    user=$2
    file=$3
    setup_environment "${conda_envs['metawrap']}"
    binning_cmd="${software_paths['metawrap']} binning -a ${file} -o ${out_dir}/${user}/4.binning -t 30 -m 100 --metabat2 --maxbin2 --concoct ${out_dir}/${user}/${user}_1.fastq ${out_dir}/${user}/${user}_2.fastq"
    run_command "$binning_cmd"
    ref_cmd="${software_paths['metawrap']} bin_refinement -o ${out_dir}/${user}/4.binning/BIN_REFINEMENT2 -t 30 -m 100 -A ${out_dir}/${user}/4.binning/metabat2_bins/ -B ${out_dir}/${user}/4.binning/maxbin2_bins/ -C ${out_dir}/${user}/4.binning/concoct_bins/ -c 50 -x 10"
    run_command "$ref_cmd"
}

# GTDB-Tk function
gtdbtk() {
    out_dir=$1
    user=$2
    setup_environment "${conda_envs['gtdbtk']}"
    if [ -d "${out_dir}/${user}/4.binning/BIN_REFINEMENT2/metawrap_50_10_bins/" ]; then
        gtdbtk_cmd="${software_paths['gtdbtk']} classify_wf --genome_dir ${out_dir}/${user}/4.binning/BIN_REFINEMENT2/metawrap_50_10_bins/ --out_dir ${out_dir}/${user}/5.gtdbtk/ --cpus 20 --extension fa"
        run_command "$gtdbtk_cmd"
        cat_gtdbtk="python ${software_paths['seqGraph']}/scripts/cat_gtdbtk.py ${out_dir}/${user}/"
        run_command "$cat_gtdbtk"
    fi
}
# AntiSmash function
antismash() {
    out_dir=$1
    user=$2
    file=$3
    setup_environment "${conda_envs['antismash']}"
    antismash_cmd="${software_paths['antismash']} -i ${file} -o ${out_dir}/${user}/6.antismash"
    run_command "$antismash_cmd"
}

# Vf and Res function
v_r_gene() {
    out_dir=$1
    user=$2
    file=$3
    setup_environment "${conda_envs['resfinder']}"
    resfinder_cmd="${software_paths['blastn']} -query ${file} -db ${database_paths['resfinder']} -out ${out_dir}/${user}/7.resfinder.out"
    run_command "$resfinder_cmd"
    setup_environment "${conda_envs['vf']}"
    vf_cmd="${software_paths['vf']} -i ${file} -o ${out_dir}/${user}/7.vf"
    run_command "$vf_cmd"
}

# Macrel function
macrel() {
    out_dir=$1
    user=$2
    file=$3
    setup_environment "${conda_envs['macrel']}"
    macrel_cmd="${software_paths['macrel']} -i ${file} -o ${out_dir}/${user}/8.macrel"
    run_command "$macrel_cmd"
}

# Main script execution
if [ $# -ne 5 ]; then
    echo "Usage: bash all.sh <out_dir> <user> <file> <task> <flag>"
    exit 1
fi

out_dir=$1
user=$2
file=$3
task=$4
flag=$5

# Check file type
data_type=$(echo "$file" | awk -F. '{print $NF}')

if [[ "$data_type" == "fastq" || "$data_type" == "fq" ]]; then
    megahit "$out_dir" "$user" "$file"
    file="${out_dir}/${user}/1.megahit/final.contigs.fa"
    seqgraph "$out_dir" "$user" "$file"
    file="${out_dir}/${user}/2.seqgraph/${user}_1000.fa"
    if [ "$flag" == "1" ]; then
        quast "$out_dir" "$user" "$file"
    fi
elif [[ "$data_type" == "fa" || "$data_type" == "fasta" ]]; then
    seqgraph "$out_dir" "$user" "$file"
    file="${out_dir}/${user}/2.seqgraph/${user}_1000.fa"
    if [ "$flag" == "1" ]; then
        quast "$out_dir" "$user" "$file"
    fi
    binning "$out_dir" "$user" "$file"
    gtdbtk "$out_dir" "$user"
fi

case "$task" in
    "second")
        antismash "$out_dir" "$user" "$file"
        ;;
    "binning")
        binning "$out_dir" "$user" "$file"
        gtdbtk "$out_dir" "$user"
        ;;
    "vf"|"res")
        v_r_gene "$out_dir" "$user" "$file"
        ;;
    "macrel")
        macrel "$out_dir" "$user" "$file"
        ;;
    *)
        echo "Invalid task: $task"
        exit 1
        ;;
esac