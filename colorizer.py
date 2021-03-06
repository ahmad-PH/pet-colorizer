import fastai
from fastai.vision import *
from fastai.callbacks import *
from fastai.utils.mem import *
from torchvision.models import vgg16_bn
import torch
import os
import sys
import wget

def load_learner_wrapper(export_directory):
	weigths_filename = 'export.pkl'
	if weigths_filename not in os.listdir('.'):
		print('model weights not found, downloading it...')
		url = "https://uce8b94e475fe5d12eb4ae54352a.dl.dropboxusercontent.com/cd/0/get/" + \
			  "AhKWWSXs5Iwz0Fzg3ySoOqdWSUg-mqasuy91m85tH5rVUq2JaBEKoJUXSs8WQKwKR-" + \
			  "T575tZk3feZaLyvVlF98YGsE2Z9P80cK8PcuE4EezzDA/file?dl=1#"
		filename = wget.download(url)
		if filename != weigths_filename:
			os.rename(filename, weigths_filename)

	return load_learner(export_directory)


def prepare_input_img(img_name):
	path = Path('./dummy-dataset/train')
	shutil.rmtree(path, ignore_errors = True)
	os.mkdir(path)
	shutil.copy(img_name, path)

	image_name = os.listdir(path)[0]
	original_size = PIL.Image.open(path/image_name).size
	min_size = min(original_size[0], original_size[1])
	rounded_min_size = min_size - (min_size % 10)

	data = (ImageImageList.from_folder('./dummy-dataset')
			.split_by_folder()
			.label_from_func(lambda x: path/x.name)
			# .transform(size=128)
			.transform(size=rounded_min_size, resize_method=ResizeMethod.SQUISH) 
			.databunch(bs=1).normalize(imagenet_stats, do_y=True))

	return data.train_ds[0][0], original_size


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("please provide the name of the image to be colorized.")
		sys.exit(1)
	
	defaults.device = torch.device('cpu')

	img, original_size = prepare_input_img(sys.argv[1])

	# arch = models.resnet34
	# learn = unet_learner(data, arch, loss_func=F.l1_loss, blur=True, norm_type=NormType.Weight)
	learn = load_learner_wrapper('.')	

	prediction = learn.predict(img)[0]

	pil_img = PIL.Image.fromarray(image2np(prediction.data * 255).astype(np.uint8))
	pil_img = pil_img.resize(original_size, PIL.Image.BILINEAR)
	pil_img.save('./result.jpg', 'JPEG')

