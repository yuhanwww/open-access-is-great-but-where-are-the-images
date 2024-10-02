import os
import csv

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(DIR_PATH, '_data', '0.NationalGalleryOfArtObjects.csv')

OUT_PATH = os.path.join(DIR_PATH, '_data', '1.object-ids.txt')

API_OBJECT_ENDPOINT = 'https://www.nga.gov/api/v1/iiif/presentation/manifest.json?cultObj:id={}'

with open(OUT_PATH, 'w') as f_out:
  # necessary to pass `encoding='utf-8-sig'` as Met csv file contains BOM
  with open(CSV_PATH, encoding='utf-8-sig') as f:
    for line in csv.DictReader(f):
      f_out.write(API_OBJECT_ENDPOINT.format(line['objectid']) + '\n')
