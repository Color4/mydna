snps = open('../output/provider/ancestry/rsids.txt')
snp_list = {}
for line in snps:
	# print()
	snp_list[line.strip()] = None#.append()

import pandas as pd

n_present = 0

strand_file = open('../input/array/InfiniumOmniExpress-24v1-3_A1_StrandReport_FDT.txt')
for line in strand_file:
	if not line.startswith('#') and not line.startswith('Index'):
		# print(line)
		# die()
		row = line.split('\t')
		# print(row)
		# die()
		snpid = row[1]
		if snpid in snp_list:
			n_present+=1

# 	if len(row)==21:
# 		if row[0] == 'IlmnID':
# 			header = line
# 		else:

print(n_present)