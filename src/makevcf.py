import gzip
dbsnp = gzip.open('../input/dbsnp/00-All.vcf.gz', 'rt')
myancestry = open('../input/provider/ancestry/AncestryDNA.txt')

variants = {}
for line in myancestry:
    if not line.startswith('#') and not line.startswith('rsid'):
        #print(line)
        row = line.strip().split('\t')
        #print(row)
        #if row[3] != '0' and row[4] != '0':
        variants[row[0]] = {
                '0':row[3],
                '1':row[4]
            }
        #die()
print('read variants')
print(len(variants))
ancestry_vcf = open('../output/provider/ancestry/Ancestry.vcf.recode.vcf')
ancestry_vcf_output = open('../output/provider/ancestry/Ancestry.genotypes.vcf', 'w')

for line in ancestry_vcf:
    #print(line)
    if not line.startswith('#'):
	row = line.split('\t')
	snp = row[2]
	ref = row[3]
	alt = row[4].split(',')
	indexes = [ref] + alt
	#print(indexes)
	#print(variants[snp])
	#print(snp)
	snp1 = variants[snp]['0']
	snp2 = variants[snp]['1']
        if snp1 not in ['0', 'I'] and snp2 not in ['0', 'I']:
	    try:

                gen1 = indexes.index(variants[snp]['0'])
                gen2 = indexes.index(variants[snp]['1'])
	        line = line.strip()+'\tGT\t{}/{}\n'.format(gen1, gen2)
	        #print(line)
	        ancestry_vcf_output.writelines(line)
            except ValueError:
		pass
    else:
	if line.startswith('#CHROM'):
            line = line.strip()+'\tFORMAT\tSample\n'
	ancestry_vcf_output.writelines(line)
#dbsnp_variants = {}
#for line in dbsnp:
#    if not line.startswith('#'):
#        #print(line)
#        row = line.split('\t')
#        dbsnp_variants[row[2]]=row[3:4]
#        #die()
#print('read dbsnp')

