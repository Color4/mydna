import os
Release = 93
from cogent.db.ensembl import HostAccount
if 'ENSEMBL_ACCOUNT' in os.environ:
    host, username, password = os.environ['ENSEMBL_ACCOUNT'].split()
    account = HostAccount(host, username, password)
else:
    account = None

from cogent.db.ensembl import HostAccount, Genome
human = Genome(Species='human', Release=Release, account=account)
variants = human.getVariation(Symbol='rs369202065')
for variant in variants:
	print(variant)
	# die()
	['AlleleFreqs', 'Alleles', 'Ancestral', 'Effect', 'FlankingSeq', 'Location', 'MapWeight', 'NULL_VALUE', 'NumAlleles', 'PeptideAlleles', 'Seq', 'Somatic', 'Symbol', 'TranslationLocation', 'Type', 'Validation', 'Variants', '__class__', '__cmp__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__len__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_attr_ensembl_table_map', '_cached', '_get_allele_freqs', '_get_allele_table_record', '_get_alleles', '_get_ancestral', '_get_ancestral_data', '_get_cached_value', '_get_effect', '_get_flanking_seq', '_get_flanking_seq_data', '_get_flanking_seq_data_ge_70', '_get_flanking_seq_data_lt_70', '_get_location', '_get_location_record', '_get_map_weight', '_get_number_alleles', '_get_peptide_variation', '_get_seq_region_record', '_get_sequence', '_get_somatic', '_get_symbol', '_get_transcript_record', '_get_translation_location', '_get_validation', '_get_variants', '_get_variation_table_record', '_location_column_prefix', '_make_location', '_populate_cache_from_record', '_set_null_values', '_split_alleles', '_table_rows', 'allele_code_table', 'allele_table', 'db', 'featureData', 'genome', 'getAnnotatedSeq', 'getFeatures', 'transcript_variation_table', 'variation_feature_table', 'variation_table']
