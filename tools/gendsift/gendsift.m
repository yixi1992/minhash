
run('vlfeat-0.9.20/toolbox/vl_setup.m')
image_dir = '/lustre/yixi/janus/frame'

%binSize = 5 ;
%magnif = 3 ;
Rwidth = 100;
Rheight = 100;

save_dir = ['/lustre/yixi/janus/dsift/bs', num2str(binSize), '_mf', num2str(magnif), '_w', num2str(Rwidth), '_h', num2str(Rheight),'/frame']

if ~exist(save_dir)
	mkdir(save_dir)
end

image_files = dir(image_dir)
for i=1:length(image_files)
	if (image_files(i).isdir), continue; end
	image_file = fullfile(image_dir, image_files(i).name)
	I = single(rgb2gray(imread(image_file)));

	% stick original image to a bigger square bounding box
	I2 = single(zeros(max(size(I))));
	I2((floor((size(I2,1)-size(I,1))/2)+1):(floor((size(I2,1)-size(I,1))/2)+size(I,1)), (floor((size(I2,2)-size(I,2))/2)+1):(floor((size(I2,2)-size(I,2))/2)+size(I,2))) = I;

	% resize the bounding box to a desired size
	I = imresize(I, [Rwidth, Rheight]);

	Is = vl_imsmooth(I, sqrt((binSize/magnif)^2 - .25)) ;

	[f, d] = vl_dsift(Is, 'size', binSize) ;
	f(3,:) = binSize/magnif ;
	f(4,:) = 0 ;
	
	[pathstr,name,ext] = fileparts(image_files(i).name);
	save_file = fullfile(save_dir, [name, '.txt'])
	fid1=fopen(save_file,'wt');
	fprintf(fid1,'%d\n',d(:));
	fclose(fid1);
end

