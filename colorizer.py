import fastai
from fastai.vision import *
from fastai.callbacks import *
from fastai.utils.mem import *
from torchvision.models import vgg16_bn
import torch
import os
import sys
import requests

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("please provide the name of the image to be colorized.")
		sys.exit(1)

	if 'export.pkl' not in os.listdir('.'):
		print('model weights not found, downloading from drive.')
		url = 'https://www.dropbox.com/s/gb81cnuuosgzgvo/export.pkl?dl=0'
		# url = 'https://drive.google.com/uc?export=download&confirm=vNFj&id=1C9bfjdn3Hy36RjUeEsfOxqzhSeaOIKTk'
		# filename = wget.download(url)
		# print(filename)
		url = 'https://drive.google.com/uc?export=download&id=1vmb1FsHOlTkR3b4VqovMwUpprOke4MEq'
		open('export.pkl', 'wb').write(requests.get(url).content)

	# defaults.device = torch.device('cpu')

	# path = Path('./images/train')
	# shutil.rmtree(path, ignore_errors = True)
	# os.mkdir(path)
	# shutil.copy(sys.argv[1], path)

	# image_name = os.listdir(path)[0]
	# original_size = PIL.Image.open(path/image_name).size
	# min_size = min(original_size[0], original_size[1])
	# rounded_min_size = min_size - (min_size % 10)

	# data = (ImageImageList.from_folder('./images')
	# 		.split_by_folder()
	# 		.label_from_func(lambda x: path/x.name)
	# 		# .transform(size=128)
	# 		.transform(size=rounded_min_size, resize_method=ResizeMethod.SQUISH) 
	# 		.databunch(bs=1).normalize(imagenet_stats, do_y=True))

	# # arch = models.resnet34
	# # learn = unet_learner(data, arch, loss_func=F.l1_loss, blur=True, norm_type=NormType.Weight)
	# learn = load_learner('.')

	# img = data.train_ds[0][0]
	# prediction = learn.predict(img)[0]

	# pil_img = PIL.Image.fromarray(image2np(prediction.data * 255).astype(np.uint8))
	# pil_img = pil_img.resize(original_size, PIL.Image.BILINEAR)
	# pil_img.save('./result.jpg', 'JPEG')

