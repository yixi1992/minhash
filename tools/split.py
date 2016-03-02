import os
import glob
import random
import numpy as np

work_dir = '/lustre/yixi/janus/dsift/bs10_mf3_w100_h100/'
dsifts = glob.glob(os.path.join(work_dir, 'frame/*'))
train_list = open(os.path.join(work_dir, 'train.list'), 'w')
test_list = open(os.path.join(work_dir, 'test.list'), 'w')

total_samples = 10000
train_to_test = 9.0/1.0


media_profile = {}
for dsift in dsifts:
	media_id = os.path.basename(dsift).split('_')[0]
	if not (media_id in media_profile):
		media_profile[media_id] = []
	media_profile[media_id].append(os.path.basename(dsift))


for media_id in media_profile:
	files = media_profile[media_id]
	n = len(files)
	if n<2:
		continue
	num_test = np.ceil(n / (train_to_test+1)).astype(np.int32)
	print 'num_test=', num_test, 'num_train=', n-num_test
	np.random.shuffle(files)
	for f in files[0:num_test]:
		test_list.write("%s\n" % f)
	for f in files[num_test:]:
		train_list.write("%s\n" % f)
	total_samples -= n
	if total_samples<0:
		break

train_list.close()
test_list.close()