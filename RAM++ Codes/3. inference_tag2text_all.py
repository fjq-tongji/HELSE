'''
 * The Tag2Text Model
 * Written by Xinyu Huang
'''
import argparse
import numpy as np
import random

import torch
import json

from PIL import Image
from ram.models import tag2text
from ram import inference_tag2text as inference
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
                    default='/data/fjq/3.VLMS/RAM+/Tag2text/tag2text_swin_14m.pth')
parser.add_argument('--image-size',
                    default=384,
                    type=int,
                    metavar='N',
                    help='input image size (default: 384)')
parser.add_argument('--thre',
                    default=0.68,
                    type=float,
                    metavar='N',
                    help='threshold value')
parser.add_argument('--specified-tags',
                    default='None',
                    help='User input specified tags')


if __name__ == "__main__":

    args = parser.parse_args()

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    transform = get_transform(image_size=args.image_size)

    # delete some tags that may disturb captioning
    # 127: "quarter"; 2961: "back", 3351: "two"; 3265: "three"; 3338: "four"; 3355: "five"; 3359: "one"
    delete_tag_index = [127, 2961, 3351, 3265, 3338, 3355, 3359]

    #######load model
    model = tag2text(pretrained=args.pretrained,
                     image_size=args.image_size,
                     vit='swin_b',
                     delete_tag_index=delete_tag_index)
    model.threshold = args.thre  # threshold for tagging

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


    Tag2text_all_results = []
    for each_img in image_paths:
        each_img_dict = {}
        image = transform(Image.open(each_img)).unsqueeze(0).to(device)
        res = inference(image, model, args.specified_tags)  #####只有英文的
        final_tags = res.split(' | ')  ######list
        each_img_dict["img_path"] = each_img
        each_img_dict["Tag2text_results"] = final_tags
        Tag2text_all_results.append(each_img_dict)
        print(each_img_dict)
        print(len(Tag2text_all_results))

    with open('Tag2text_results_0.6.json', 'w') as f:
        json.dump(Tag2text_all_results, f, indent=4)



















    #######load model
    # model = tag2text(pretrained=args.pretrained,
    #                          image_size=args.image_size,
    #                          vit='swin_b',
    #                          delete_tag_index=delete_tag_index)
    # model.threshold = args.thre  # threshold for tagging
    # model.eval()
    #
    # model = model.to(device)
    #
    # image = transform(Image.open(args.image)).unsqueeze(0).to(device)
    #
    # res = inference(image, model, args.specified_tags)
    # print("Model Identified Tags: ", res[0])
    # print("User Specified Tags: ", res[1])
    # print("Image Caption: ", res[2])
