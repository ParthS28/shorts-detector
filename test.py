import json
import os

anno = json.load(open(os.path.join('dataset/val', "via_region_data.json")))
anno = anno['_via_img_metadata']
anno = json.dumps(anno)
print(type(anno))
print(anno)


