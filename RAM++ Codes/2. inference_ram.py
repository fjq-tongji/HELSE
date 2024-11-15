'''
 * The Recognize Anything Model (RAM)
 * Written by Xinyu Huang
'''
import argparse
import numpy as np
import random

import torch
import json

from PIL import Image
from ram.models import ram
from ram import inference_ram as inference
from ram import get_transform


parser = argparse.ArgumentParser(
    description='Tag2Text inferece for tagging and captioning')
parser.add_argument('--image',
                    metavar='DIR',
                    help='path to dataset',
                    default='/data/fjq/3.VLMS/CODA2022/images_total/')
parser.add_argument('--pretrained',
                    metavar='DIR',
                    help='path to pretrained model',
                    default='/data/fjq/3.VLMS/RAM+/RAM/ram_swin_large_14m.pth')
parser.add_argument('--image-size',
                    default=384,
                    type=int,
                    metavar='N',
                    help='input image size (default: 384)')


if __name__ == "__main__":

    args = parser.parse_args()

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    transform = get_transform(image_size=args.image_size)

    #######load model
    model = ram(pretrained=args.pretrained,
                             image_size=args.image_size,
                             vit='swin_l')
    model.eval()

    model = model.to(device)

    #####load_imgs
    # image_paths = [os.path.join(args.image, fname) for fname in os.listdir(args.image)]
    image_paths = []
    with open('./Ours_llava_7b_detail_caption_entity_1.json', 'r', encoding='utf-8') as file:
        captions = json.load(file)  ###我们自己的全部描述，这个顺序
    for k in range(len(captions)):
        img_name = captions[k]['img_path']
        image_paths.append(img_name)
    #########################################################################

    ram_all_results = []
    for each_img in image_paths:
        each_img_dict = {}
        image = transform(Image.open(each_img)).unsqueeze(0).to(device)
        res = inference(image, model)  #####只有英文的
        final_tags = res.split(' | ')  ######list
        each_img_dict["img_path"] = each_img
        each_img_dict["ram_results"] = final_tags
        ram_all_results.append(each_img_dict)
        print(each_img_dict)
        print(len(ram_all_results))

    with open('RAM_results_0.6.json', 'w') as f:
        json.dump(ram_all_results, f, indent=4)


