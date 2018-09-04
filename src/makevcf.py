import gzip
dbsnp = gzip.open('/projects/data/dbsnp/00-All.vcf.gz', 'rt')
myancestry = open('/projects/mydna/input/provider/ancestry/AncestryDNA.txt')

variants = {}
for line in myancestry:
    if not line.startswith('#') and not line.startswith('rsid'):
        #print(line)
        row = line.strip().split('\t')
        #print(row)
        variants[row[0]] = {
                '0':row[3],
                '1':row[4]
            }
        #die()
print('read variants')
dbsnp_variants = {}
for line in dbsnp:
    if not line.startswith('#'):
        #print(line)
        row = line.strip().split('\t')
        dbsnp_variants[row[2]]=row
        #die()
