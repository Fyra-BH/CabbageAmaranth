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
- **标注工具**: 使用[Labelme](https://github.com/wkentaro/labelme)软件进行标注。
- **数据集格式**: 标注后的数据已转换为YOLO数据集格式，并使用CloDSA进行图像增强。

## 数据集结构

```
dataset/
├── images/
│   ├── 0_0_000001.jpg
│   ├── ...
│   ├── 89_3_000090.jpg
└── labels/
    ├── 0_0_000001.txt
    ├── ...
    └── 89_3_000090.txt
```

## 使用方法

以ultralytics出品的yolov8项目为例：

1. 将本repo下载至ultralytics数据集指定位置，一般是用户目录下的\Ultralytics\datasets
2. 编写yaml配置文件，例子会在后面给出
3. 使用数据集训练模型

一个yaml的例子：CabbageAmaranth.yaml

```yaml
path: ../datasets/CabbageAmaranth # dataset root dir
train: images # train images 
val: images # val images
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
