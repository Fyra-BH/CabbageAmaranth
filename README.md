# CabbageAmaranth

# 小白菜与红叶苋数据集

## 简介

本数据集旨在为作物幼苗识别和分类提供视觉数据支持，特别是针对京研快菜（青梗小白菜）和红叶苋。数据集包含两种作物的幼苗图片，收集于2024年1月至3月期间。

## 数据集内容

- **作物种类**:

  - **白菜**（cabbage）
  - **红叶苋**（amaranth）
- **图片收集时间**: 2024年1月底至3月
- **图片来源**: 使用手机拍摄的原图，分辨率为3648x2736
- **处理方法**: 使用Python脚本裁剪成1080p分辨率的图片，脚本命令如下：

  ```
  python crop_images.py --input_dir /path/to/image_dir --output_dir output_dir
  ```

  crop_images.py一种实现：

  ```python
  import argparse
  import os
  from PIL import Image

  def crop_image(image_path, output_path, width=1920, height=1080):
      image = Image.open(image_path)
      img_width, img_height = image.size

      for i in range(img_width // width):
          for j in range(img_height // height):
              box = (i * width, j * height, (i + 1) * width, (j + 1) * height)
              cropped_img = image.crop(box)
              cropped_img.save(os.path.join(output_path, f'cropped_{i}_{j}_{os.path.basename(image_path)}'))

  def main():
      parser = argparse.ArgumentParser(description='Crop images to 1080p.')
      parser.add_argument('--input_dir', type=str, required=True, help='Directory of images to be cropped.')
      parser.add_argument('--output_dir', type=str, required=True, help='Directory to save cropped images.')
      args = parser.parse_args()

      if not os.path.exists(args.output_dir):
          os.makedirs(args.output_dir)

      for filename in os.listdir(args.input_dir):
          if filename.endswith(('.jpg', '.png', '.jpeg')):
              crop_image(os.path.join(args.input_dir, filename), args.output_dir)

  if __name__ == '__main__':
      main()

  ```
- **标注工具**: 使用[Labelme](https://github.com/wkentaro/labelme)软件进行标注。
- **数据集格式**: 标注后的数据已转换为YOLO数据集格式，并使用CloDSA进行图像增强。

## 数据集结构

```
CabbageAmaranth/
├── images
│   ├── train
│   │   ├── 0_0_00000.jpg
│   │   ├── ...
│   │   └── 567_0_00567.jpg
│   └── val
│       ├── 5_0_00005.jpg
│   │   ├── ...
│       └── 647_3_00647.jpg
└── labels
    ├── train
    │   ├── 0_0_00000.txt
    │   ├── ...
    │   └── 567_0_00567.txt
    └── val
        ├── 5_0_00005.txt
        ├── ...
        └── 647_3_00647.txt
```

## 使用方法

以ultralytics出品的yolov8项目为例：

1. 将本repo下载至ultralytics数据集指定位置，一般是用户目录下的\Ultralytics\datasets
2. 编写yaml配置文件，例子会在后面给出
3. 使用数据集训练模型

一个yaml的例子：CabbageAmaranth.yaml

```yaml
path: ../datasets/CabbageAmaranth # dataset root dir
train: images/train # train images
val: images/val # val images
test: # test images (optional)

# Classes
names:
  0: cabbage
  1: amaranth
```

## 许可证和使用限制

本数据集遵循MIT。在使用数据集前，请确保您了解并遵守许可证条款。

## 贡献和反馈

如果您在使用数据集时遇到问题，或有任何改进建议，请通过2101210218@stu.edu.pku.cn与我们联系。
