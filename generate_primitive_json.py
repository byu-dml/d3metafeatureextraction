import json

from d3metafeatureextraction import D3MetafeatureExtraction

outfile = "primitive.json"
with open(outfile, "w") as f:
	primitive_json = D3MetafeatureExtraction(hyperparams=None).metadata.to_json()
	f.write(json.dumps(primitive_json, indent=4))
