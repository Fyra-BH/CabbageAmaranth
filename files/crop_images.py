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
