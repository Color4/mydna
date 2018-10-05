ancestry = '/home/raony.guimaraes/dev/mydna/input/providers/ancestry/AncestryDNA.txt'

meand23 = '/home/raony.guimaraes/dev/mydna/input/providers/23andme/genome_Raony_GuimaraesCorreaDOCarmoLisboCardenas_v5_Full_20180930031157.txt'

ancestry_positions = []
ancestry_snps = []
ancestry_genotypes = {}

ancestry_file = open(ancestry)
for line in ancestry_file:
	if not line.startswith('#') and not line.startswith('rsid'):
		# print(line)
		row = line.strip().split('\t')
		ancestry_snps.append(row[0])

		if row[1] == '23':
			row[1] = 'X'
		if row[1] == '24':
			row[1] = 'Y'
		if row[1] == '26':
			row[1] = 'MT'
		
		index = '{}-{}'.format(row[1], row[2])
		ancestry_positions.append(index)
		genotype = '{}{}'.format(row[3], row[4])
		if len(genotype) != 2:
			# print('found', row)
			genotype = '{}{}'.format(row[3],row[3])
		ancestry_genotypes[index] = {}
		ancestry_genotypes[index]['genotypes'] = ''.join(sorted(genotype))
		ancestry_genotypes[index]['index'] = index


print('ancestry_positions', len(ancestry_positions))

meand23_positions = []
meand23_snps = []
meand23_genotypes = {}

meand23_file = open(meand23)
for line in meand23_file:
	if not line.startswith('#'):	
		# print(line)
		row = line.strip().split('\t')
		meand23_snps.append(row[0])
		index = '{}-{}'.format(row[1], row[2])
		meand23_positions.append(index)

		# meand23_genotypes
		genotype = row[3]

		if len(genotype) == 1:
			# print('found', row)
			genotype = '{}{}'.format(row[3],row[3])
		meand23_genotypes[index] = {}
		meand23_genotypes[index]['genotypes'] = ''.join(sorted(genotype))
		meand23_genotypes[index]['index'] = index


common_snps = list(set(ancestry_snps) & set(meand23_snps))
common_positions = list(set(ancestry_positions) & set(meand23_positions))
n_commmon=len(common_snps)

print('meand23_positions', len(meand23_positions))
print('common positions', len(common_positions))
print('common rsids', n_commmon)

n_concordant = 0
#concordance
discordant = open('discordant_snps.txt', 'w')
for snp in common_positions:
	# print(snp)
	if ancestry_genotypes[snp]['genotypes'] == meand23_genotypes[snp]['genotypes']:
		n_concordant+=1
	else:
		discordant.writelines('\t'.join([snp, ancestry_genotypes[snp]['genotypes'], ancestry_genotypes[snp]['index'],  meand23_genotypes[snp]['genotypes'], meand23_genotypes[snp]['index']])+'\n')
		# print(snp, ancestry_genotypes[snp], meand23_genotypes[snp])

print('n_concordant', n_concordant)
print('concordance', (float(n_concordant)/n_commmon)*100)
