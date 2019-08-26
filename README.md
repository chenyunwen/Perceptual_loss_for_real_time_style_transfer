Pytorch implementation of "Perceptl Losses for Real-Time Style Transfer and Super-Resolution"
---

Pytorch implementation of the paper:
"Perceptual Losses for Real-Time Style Transfer and Super-Resolution"

Justin Johnson, Alexandre Alahi, Li Fei-Fei 

ECCV 2016

Dependencies
--
* Pytorch (version >= 0.4.0)

Download
--
* The trained models can be downloaded throuth the [Google drive](https://drive.google.com/drive/folders/1_FjrtNgVGgstMFRIY6K_Fp3w1K96Zpn5?usp=sharing).
* [MSCOCO train2014](http://cocodataset.org/#download) is needed to train the network.

Usage
--

### Train example script

```
python main.py --train-flag True --cuda-device-no 0 --imsize 256 --cropsize 240 --train-content-image-path ./coco2014/ --train-style-image-path sample_images/style_images/mondrian.jpg --save-path trained_models/
```

### Test example script

```
python main.py --train-flag False --cuda-device-no 0 --imsize 256 --model-load-path trained_models/network.pth --test-image-path sample_images/content_images/chicago.jpg --output-image-path stylized.png
```
