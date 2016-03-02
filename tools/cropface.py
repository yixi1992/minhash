import csv
import os
from PIL import Image
from PIL import ImageFile

image_dir = '/lustre/yixi/janus'
save_dir = 'janus_face'

ImageFile.LOAD_TRUNCATED_IMAGES = True
with open('metadata.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		file = row['FILE']
		media_id = row['MEDIA_ID']
		face_x = int(round(float(row['FACE_X'])))
		face_y = int(round(float(row['FACE_Y'])))
		face_width = int(round(float(row['FACE_WIDTH'])))
		face_height = int(round(float(row['FACE_HEIGHT'])))
		
		image_path = os.path.join(image_dir, file)
		save_file = os.path.join(save_dir, file)
		print image_path, os.path.isfile(image_path)
		if os.path.isfile(image_path) and not os.path.isfile(save_file):
			img = Image.open(image_path)
			print 'cropping (', face_x, face_y, face_x+face_width, face_y+face_height, ') from', img.size
			img2 = img.crop((face_x, face_y, face_x+face_width, face_y+face_height))
			print 'cropped and saving to ', save_file
			img2.save(save_file)
