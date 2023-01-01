# Perceptual Losses for Real-Time Style Transfer

Reference repository: https://github.com/tyui592/Perceptual_loss_for_real_time_style_transfer.git

## What we did?
1. Modified to do video style transfer.
2. Calculate execution time.

## How to use?

Environment we used:
- [Python 3.10.8]
- [PyTorch 1.13.1]

### Run this code:

#### Training

We use [MSCOCO train2014](http://cocodataset.org/#download) as training data and put the training images in `./coco2014`.

Example for training with style image `imgs/style/Arles.jpg`:
```
python main.py --train-flag True --cuda-device-no 0 --imsize 256 --cropsize 240 --train-content ./coco2014/ --train-style imgs/style/Arles.jpg --save-path trained_models/Arles/
```

#### Testing

We trained four models named `transform_network.pth`, respectively in the following folders:

`trained_models/the-muse/`, `trained_models/wave/`, `trained_models/starry_night/`, `trained_models/Arles/`

- Image style transfer example

```
python main.py --train-flag False --cuda-device-no 0 --imsize 256 --model-load-path trained_models/Arles/transform_network.pth --test-content imgs/image_0.jpg --output RealTime_Arles_S256_E10000_image_0.jpg
```
- Video style transfer example

```
python main.py --train-flag False --cuda-device-no 0 --imsize 256 --model-load-path trained_models/the-muse/transform_network.pth --input-video imgs/video_0.mp4 --output-video trained_models/the-muse/video_0.mp4
```

## Our result

- input styles

<img src ="imgs\style\the-muse.jpg" height="128px" /> <img src ="imgs\style\Under-the-Wave-off-Kanagawa.jpg" height="128px" /> <img src ="imgs\style\starry_night.jpg" height="128px" /> <img src ="imgs\style\Arles.jpg" height="128px" />

### Image style transfer
- input content image

<img src ="imgs\image_0.jpg" height="128px"/> <img src ="imgs\image_1.jpg" height="128px"/>

- Result

<img src ="Result\RealTime_the-muse_S256_E10000_chicken.jpg" height="128px" /> <img src ="Result\RealTime_the-muse_S256_E10000_image_1.png" height="128px" /> <img src ="Result\RealTime_wave_S256_E10000_chicken.jpg" height="128px" /> <img src ="Result\RealTime_wave_S256_E10000_image_1.png" height="128px" /> 

<img src ="Result\RealTime_night_S256_E10000_chicken.jpg" height="128px" /> <img src ="Result\RealTime_night_S256_E10000_image_1.jpg" height="128px" /> <img src ="Result\RealTime_Arles_S256_E10000_image_0.jpg" height="128px" /> <img src ="Result\RealTime_Arles_S256_E10000_image_1.jpg" height="128px" /> 

### Video style transfer
- input content video
`imgs/video_0.mp4` and `imgs/video_1.mp4`

- Result
`trained_models/style_name/style_name_video_0.mp4` and `trained_models/style_name/style_name_video_1.mp4`
---

## The following content comes from the original Repository.
<!-- --- -->
**Unofficial PyTorch implementation of real-time style transfer**

**Reference**: [Perceptual Losses for Real-Time Style Transfer and Super-Resolution, ECCV2016](https://arxiv.org/abs/1603.08155)

**Contact**: `Minseong Kim` (tyui592@gmail.com)

Requirements
--
* Pytorch (version >= 0.4.0)
* Pillow

Download
--
* The trained models can be downloaded throuth the [Google drive](https://drive.google.com/drive/folders/1_FjrtNgVGgstMFRIY6K_Fp3w1K96Zpn5?usp=sharing).
* [MSCOCO train2014](http://cocodataset.org/#download) is needed to train the network.

Usage
--

### Arguments

* `--train-flag`: Flag for train or evaluate transform network
* `--train-content`: Path of content image dataset (MSCOCO is needed)
* `--train-style`: Path of a target style image 
* `--test-content`: Path of a test content image
* `--model-load-path`: Path of trained transform network to stylize the `--test-content` image

### Train example script

```
python main.py --train-flag True --cuda-device-no 0 --imsize 256 --cropsize 240 --train-content ./coco2014/ --train-style imgs/style/mondrian.jpg --save-path trained_models/
```

### Test example script

```
python main.py --train-flag False --cuda-device-no 0 --imsize 256 --model-load-path trained_models/transform_network.pth --test-content imgs/content/chicago.jpg --output stylized.png
```

Results
--


![test_result](https://github.com/tyui592/Perceptual_loss_for_real_time_style_transfer/blob/master/imgs/figure1.png)

