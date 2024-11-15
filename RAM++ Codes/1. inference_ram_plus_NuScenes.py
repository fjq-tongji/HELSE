'''
 * The Recognize Anything Plus Model (RAM++)
 * Written by Xinyu Huang
'''
import argparse
import numpy as np
import random
import os
import torch
import json
from PIL import Image
from ram.models import ram_plus
from ram import inference_ram as inference
from ram import get_transform


parser = argparse.ArgumentParser(
    description='Tag2Text inferece for tagging and captioning')
parser.add_argument('--image',
                    metavar='DIR',
                    help='path to dataset',
                    default='/data/nuscenes_dataset/samples/CAM_FRONT/')
parser.add_argument('--pretrained',
                    metavar='DIR',
                    help='path to pretrained model',
                    default='/data/fjq/3.VLMS/RAM+/ram_plus_swin_large_14m.pth')
parser.add_argument('--image-size',
                    default=384,
                    type=int,
                    metavar='N',
                    help='input image size (default: 448)')


if __name__ == "__main__":

    args = parser.parse_args()

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    transform = get_transform(image_size=args.image_size)

    #######load model
    model = ram_plus(pretrained=args.pretrained,
                             image_size=args.image_size,
                             vit='swin_l',
                             #threshold=0.48
                             )
    model.eval()

    model = model.to(device)

    #####load_imgs
    # image_paths = [os.path.join(args.image, fname) for fname in os.listdir(args.image)]
    image_paths = []
    captions = []
    with open('./POPE_nuscenes.json', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                # 解析每一行的JSON数据
                item = json.loads(line)
                captions.append(item)

        # captions = json.load(file)            ###我们自己的全部描述，这个顺序


    for k in range(len(captions)):
        img_name_ = captions[k]['image']
        img_name = '/data/nuscenes_dataset/samples/CAM_FRONT/' + img_name_
        image_paths.append(img_name)
    #########################################################################


    ram_plus_all_results = []
    for each_img in image_paths:
        each_img_dict = {}
        image = transform(Image.open(each_img)).unsqueeze(0).to(device)
        res = inference(image, model)    #####只有英文的
        final_tags = res.split(' | ')    ######list
        each_img_dict["img_path"] = each_img
        each_img_dict["ram_plus_results"] = final_tags
        ram_plus_all_results.append(each_img_dict)
        print(len(ram_plus_all_results))


    with open('RAM_plus_results_NuScenes.json', 'w') as f:
        json.dump(ram_plus_all_results, f, indent=4)






