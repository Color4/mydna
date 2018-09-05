snps = open('../output/provider/ancestry/rsids.txt')
snp_list = {}
for line in snps:
	# print()
	snp_list[line.strip()] = None#.append()

import pandas as pd

n_present = 0

strand_file = open('../input/array/InfiniumOmniExpress-24v1-3_A1.csv')
for count, line in enumerate(strand_file, 1):
	# print(line)
	row = line.split(',')
	# if count % 50000 == 0:
	# 	print(count, n_present)
	if len(row)==21:
		if row[0] == 'IlmnID':
			header = line
		else:
			snpid = row[1]
			if snpid in snp_list:
				# print(snpid)
				n_present+=1

print(n_present)