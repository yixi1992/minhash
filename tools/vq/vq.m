

binSize = 20 ;
magnif = 3 ;
Rwidth = 100;
Rheight = 100;

work_dir = ['/lustre/yixi/janus/dsift/bs', num2str(binSize), '_mf', num2str(magnif), '_w', num2str(Rwidth), '_h', num2str(Rheight)]
sift_dir = [work_dir, '/frame']
vq_dir = [work_dir, '/vq']

% K for k-means
%K = 65536
%frame_per_media = 10;
K = 256
frame_per_media = 1;


sift_files = dir(sift_dir);
sift_files([sift_files.isdir]) = []; 	

data = np.zeros(128, frame_per_media*length(sift_files));
for i=1:length(sift_files),
	sift_file = fullfile(sift_dir, sift_files(i).name)
	load(sift_file)
	P = randperm(size(d,2), frame_per_media);
	data(:, ((i-1)*frame_per_media+1):(i*frame_per_media)) = d(:, P);
end


data = single(data');

[IDX, C] = kmeans(data, K);
save(fullfile(work_dir, 'kmeans_centroids.mat'), 'C')

for i=1:length(sift_files),
	sift_file = fullfile(sift_dir, sift_files(i).name)
	load(sift_file)
	vq = np.zeros(K, 1);
	for j=1:size(D,2)
		dis = sum((repmat(D(:,j)', K, 1)-C).^2, 2);
		[x, idx] = min(dis);
		vq(idx) = 1;
	end
	fid = fopen(fullfile(vq_dir, sift_files(i).name),'wt');
	fprintf(fid,'%d', vq);
	fclose(fid);
end

