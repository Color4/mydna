import os
import numpy as np

dna_file = open('/projects/mydna/input/provider/ancestry/AncestryDNA.txt')
rsids = []
positions = []
for line in dna_file:
    if not line.startswith('#') and not line.startswith('rsid'):
        row = line.split('\t')
        rsids.append(row[0])
#        positions.append('{}\t{}\t{}'.format(row[1], int(row[2])-1, row[2]))
#
#rsfile = open('/projects/mydna/output/provider/ancestry/rsids.txt', 'w')
#for rsid in rsids:
#    rsfile.writelines(rsid+'\n')
#rsfile.close()
#
#posfile = open('/projects/mydna/output/provider/ancestry/positions.bed', 'w')
#
#for pos in positions:
#    posfile.writelines(pos+'\n')
#posfile.close()

os.chdir('/projects/mydna/output/provider/ancestry/')
#command = 'bcftools view -v snps -R positions.bed /projects/data/1000genomes/ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.wgs.phase3_shapeit2_mvncall_integrated_v5b.20130502.sites.vcf.gz -o ancestrysnps.vcf -O v'
#os.system(command)

import gzip

genome1k_snps = []

with gzip.open('/projects/data/dbsnp/00-All.vcf.gz', 'rt') as f:
    for line in f:
        if not line.startswith('#'):
            row = line.split('\t')
            genome1k_snps.append(row[2])

print('Finished loading 1k snps')
#for snp in rsids:
#    if snp not in genome1k_snps:
#        print(snp)
#        die()
#print(list(set(rsids)-set(genome1k_snps)))


a1 = np.array(rsids)
a2 = np.array(genome1k_snps)
ct = np.setdiff1d(a1, a2)
#ct = np.sum(a1!=a2)
print(ct)


