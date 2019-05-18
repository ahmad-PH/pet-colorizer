# Pet Colorizer

This application will accept an input grayscale image of a pet (it only can handle dogs and cats for now), and colorize it for you! It was created using the [fast.ai](https://docs.fast.ai) library, and most of its code actually comes from [Lesson 7](https://course.fast.ai/videos/?lesson=7) of the fastai course. My main contribution has been to change the model introduced in the course from being an image restorer (turning low resolution images to high resolution ones) to an image colorizer. Also, I wrote a python script that encapsulates the whole AI stuff inside and directly converts an input image file into a colorized output image file.

Here are some examples of what this application can do:

<p style="clear: both">
<img src="./github-images/cat1.jpeg">
<img src="./github-images/prediction/cat1.jpg">
<br/>

<img src="./github-images/cat11.jpg" width="400px" height="400px">
<img src="./github-images/prediction/cat11.jpg" width="400px" height="400px">
<br/>

<img src="./github-images/dog5.jpeg">
<img src="./github-images/prediction/dog5.jpg">
<br/>

<img src="./github-images/dog10.jpg" width="400px" height="300px">
<img src="./github-images/prediction/dog10.jpg" width="400px" height="300px">
<br/>

## Getting Started

Unfortunately, I haven't had the chance to turn this project into a web application yet, due to [Now-Zeit](https://zeit.co/now) changing their API in a way that [breaks all fastai deployments](https://course.fast.ai/deployment_zeit.html), and being unable to find any other free deployment services to quickly deploy my application. But I will be working on it, and will change the repo to reflect any changes that I'm able to make.

For now, if you want to try colorizing some photos yourself you have to clone the project, change directory to its root directory and then run
```
python colorizer.py <filename-of-grayscale-image>
```
the application will then create the colorized image in its root directory (which should be your current directory).

Please Note that the first time you run the "colorizer" script, it will attempt to download the model (as github wouldn't allow for such a huge file to be uploaded) and that might take a while (the download size is approximately 250MB).

### Prerequisites

You will need to install the [fast.ai](https://docs.fast.ai/install.html) library as well as [python-wget](https://pypi.org/project/wget) to run this project. Note that you do not need to use the GPU for running this project, so don't bother setting up the environment for it if you haven't done so already.

## Authors

* **Ahmad Pourihosseini** - [ahmad-PH](https://github.com/ahmad-PH)

## Acknowledgments

* Thanks to all the amazing people at [fast.ai](https://docs.fast.ai/) who have made creating such projects a breeze :)

