# https://pypi.org/project/pyensemblrest/
from ensemblrest import EnsemblRest
ensRest = EnsemblRest()

print ensRest.getVariationById(id="rs56116432", species="homo_sapiens")
# print ensRest.getVariationByMultipleIds(ids=["rs56116432", "COSM476" ], species="homo_sapiens")