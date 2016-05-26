import os
import glob
import random
import numpy as np
import matplotlib.pyplot as plt
#/lustre/yixi/janus/dsift/bs5_mf3_w100_h100 vq_K1024_fpm4
work_dir = '/lustre/yixi/janus/dsift/'
dsifts = glob.glob(os.path.join(work_dir, 'bs5_mf3_w100_h100/vq_K1024_fpm4/*'))


media_profile = {}
for dsift in dsifts:
	media_id = os.path.basename(dsift).split('_')[0]
	if not (media_id in media_profile):
		media_profile[media_id] = []
	media_profile[media_id].append(dsift)


def plothist(save_path, hist):
	plt.clf()
	plt.hist(hist)
	plt.title(os.path.basename(save_path))
	plt.savefig(save_path)



def computehist():
	hist = []
	for media_id in media_profile:
		files = media_profile[media_id]
		n = len(files)
		if n<2:
			continue
		for f in files:
			bc = open(f, 'r').read()
			cnt = sum(bc[i]=='1' for i in range(0, len(bc)))
			print cnt
			hist.append(cnt)

	print np.mean(hist)
	plothist(os.path.join(work_dir, 'hist'), hist)



def calciou(f1, f2):
	bc1 = open(f1, 'r').read()
	bc2 = open(f2, 'r').read()
	int = 0
	uni = 0
	for i in range(0, len(bc1)):
		if bc1[i]=='1'and bc2[i]=='1':
			int+=1
			uni+=1
		elif bc1[i]=='1' or bc2[i]=='1':
			uni+=1
	return int*1.0/uni


def computedist():
	hist_intra = []
	hist_inter = []
	i =1
	while i<10000000:
		i+=1
		k1 = random.choice(media_profile.keys())
		k2 = random.choice(media_profile.keys())
		f1 = random.choice(media_profile[k1])
		f2 = random.choice(media_profile[k2])

		iou = calciou(f1, f2)
		print i, 'inter', iou
		hist_inter.append(iou)

		f2 = random.choice(media_profile[k1])
		iou = calciou(f1, f2)
		hist_intra.append(iou)
		print i, 'intra', iou
		
		
		if i % 10000 ==0:
			plothist(os.path.join(work_dir, 'intra_class'), hist_intra)
			plothist(os.path.join(work_dir, 'inter_class'), hist_inter)

def computeclustersize():
	hist = np.zeros(1024)
	for media_id in media_profile:
		files = media_profile[media_id]
		n = len(files)
		if n<2:
			continue
		for f in files:
			bc = open(f, 'r').read()
			for i in range(0, len(bc)):
				if bc[i]=='1':
					hist[i]+=1
	
	plt.clf()
	hist = sorted(hist)
	plt.bar(range(0, len(hist)), hist)
	plt.ylabel('cluster size')
	plt.title(os.path.basename('clustr size'))
	plt.savefig(os.path.join(work_dir, 'cluster_size'))



#computehist()
#computedist()
computeclustersize()

