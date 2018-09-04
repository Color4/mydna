import os

dna_file = '../provider/ancestry/dna-data-2018-08-27.zip'

command = 'unzip {} -d ../provider/ancestry/'.format(dna_file)
# os.system(command)

ancestry_file = open('../provider/ancestry/AncestryDNA.txt')

snps = []
for line in ancestry_file:
	if not line.startswith('#') and not line.startswith('rsid'):
		row = line.strip().split('\t')
		# print(row)
		snps.append(row[0])

# print(len(snps)/2)
# def chunks(l, n):
#     """Yield successive n-sized chunks from l."""
#     for i in range(0, len(l), n):
#         yield l[i:i + n]

# snp_chunks = chunks(snps,1000)
# #query snps
# for count, snp_chunk in enumerate(snp_chunks, 1):
# 	command = """mysql -B --user=genome --host=genome-mysql.cse.ucsc.edu -A -D hg38 -e 'select * from snp150 where name in ("{}")' > ../data/ancestrydna.{}.tsv""".format("\", \"".join(snp_chunk), count)
# 	# print(command)
# 	os.system(command)
# 	# die()

#get from dbsnp vcf