
# 1.Obtain project
```
git clone https://github.com/Tecot/dsm-server.git
```

# 2.Migration object
```
python manage.py makemigrations
python manage.py migrate
```

# 3.Configuration environment
### Main environment
```
conda create --name <your_conda_name> python=3.9
conda activate <your_conda_name>
cd dsm-center
pip install -r requirements.txt
```
### Other environment
```
antismash:
conda create --name antismash antismash=7.1.0
metawrap:
conda create --name metawrap metawrap=1.3.2
gtdbtk:
conda create --name gtdbtk gtdbtk=2.1.0
```

# Database
```
Open the settings. py file in the project and change the database path in the Database struct.

Database path:
DATABASE_PATH = '/home/tecot/projects/dsm/database'

Database struct
# -
# database
# ----SRP123456
# --------anntation
# ------------SRP123456.faa
# --------pro_str
# ------------SRP123456_13456.pdb
# ------------SRP123457_13456.pdb
# ------------...
# --------final_contigs.fa
# --------resfinder.tab
# --------vfdb.tab
# --------SRP123456.gbk
# --------SRP123456.tsv
# --------gtdbtk.bac120.summary.tsv
# --------metawrap_50_10_bins.contigs
# --------metawrap_50_10_bins.stats
# --------macrel.out.prediction 
# --------SRP121432_combined.csv


```

# 4.Configuration softwares
### bwa
```
Link: git clone https://github.com/lh3/bwa.git
Note: Install according to software requirements('make' compile)
```
### samtools
```
Link: wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2
Note: Install according to software requirements
```
### megahit
```
Link: git clone https://github.com/voutcn/megahit.git
Note: Install according to software requirements('make' compile. https://zhuanlan.zhihu.com/p/470457258)
```
### blastn
```
Link: wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.9.0/ncbi-blast-2.9.0+-x64-linux.tar.gz
Note: Install according to software requirements
```
### quast
```
Link: wget -c https://github.com/ablab/quast/releases/download/quast_5.2.0/quast-5.2.0.tar.gz
Note: Install according to software requirements
```
### seqGraph
```
Link: 
Note: Install according to software requirements
```



# Start project
## Manual start project
### Step 1: Run project
```
python manage.py runserver
```
### Step 2: Run celery worker
```
celery -A server worker --loglevel=info
```

## Shell start project
```
./run.sh
```





