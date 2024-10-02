import os
import json
from tqdm import tqdm
import csv

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
JSON_DIR_PATH = os.path.join(DIR_PATH, '_data', '2.object-json-data')
CSV_FILE_PATH = os.path.join(DIR_PATH, '..', '..', '1.data', 'nga-images.csv')

# Transform title string to formatted string in image url for later use
def transform_string(s):
  s = s.lower()
  s = s.replace(' ', '_')
  s = s.replace(',', '%2C')
  s = s.replace('[', '__').replace(']', '__')
  return s

all_object_images = []

for file_name in tqdm(os.listdir(JSON_DIR_PATH)):
  file_path = os.path.join(JSON_DIR_PATH, file_name)
  with open(file_path) as f:
    data = json.load(f)

  # Get object id
  object_id_url = data.get('@id')
  object_id = object_id_url.split("id=")[1] # only keep the numeric part in id url
  assert object_id

  if data['metadata']: 
    # Get object accession number
    object_accession_number = data["metadata"][1]["value"]
    assert object_accession_number

    # Get object title
    object_title = data["metadata"][3]["value"]
    assert object_title

    assert data.get('sequences'), file_name
    assert len(data['sequences']) == 1, file_name
    if not data['sequences'][0].get('canvases'):
        # no images at all
        continue

    assert data['sequences'][0].get('canvases')[0].get('images'), file_name
    canvases = data['sequences'][0].get('canvases')
    assert len(canvases[0]['images']) == 1, file_name
    images = canvases[0].get('images')
    assert images[0].get('resource'), file_name
    resource = images[0].get('resource')
    assert images[0]['resource'].get('service'), file_name
    assert images[0]['resource'].get('service').get('@id'), file_name
    image_id = images[0]['resource'].get('service').get('@id')
    assert image_id

    # compile img url with id and title
    image_url = image_id + '/full/full/0/default.jpg?attachment_filename=' + transform_string(object_title) + '_' + object_accession_number + '.jpg'

    all_object_images.append({
        'object_id': object_id,
        'image_url': image_url
    })

# Writing to CSV file
with open(CSV_FILE_PATH, 'w') as f:
  writer = csv.DictWriter(f, fieldnames=('object_id', 'image_url'))
  writer.writeheader()

  for object_image in all_object_images:
    writer.writerow({
      'object_id': object_image['object_id'],
      'image_url': object_image['image_url']
    })
