import os
#os.environ["CUDA_VISIBLE_DEVICES"]="6"
import torch
from typing import Dict


class Groundingdino_words_you_update:
    def __init__(self, args):
        self.args = args
    

    def groundingdino_words_update(self, sample: Dict, pipeline):
        # ################# 1. 先把blip2和instructblip的结果合并在一起
        # nouns_blip2 = sample['ram_plus_nouns_groundingdino_blip2']
        # nouns_instructblip = sample['ram_plus_nouns_grounding_instructblip']
        # final = []
        # for each_word in nouns_blip2:
        #     if each_word not in final:
        #         final.append(each_word)
        #
        # for each_word in nouns_instructblip:
        #     if each_word not in final:
        #         final.append(each_word)


        final = sample['YOLO11_x_results']      #sample['Tag2text_results']      #sample['ram_plus_nouns_groundingdino']
        ################# 2. 利用右分支对左分支进行过滤
        you_branch_yuan = sample['named_entity_blip2_instructblip_update']
        final_groundingdino_results = []
        #######################################先把右边分支的所有实体整合到一个列表中
        you_branch_total = []
        for each_line in you_branch_yuan:
            if '.' in each_line:
                each_line_ = each_line.split('.')
                you_branch_total.extend(each_line_)
            elif '.' not in each_line and 'None' not in each_line and 'No this word' not in each_line:
                you_branch_total.append(each_line)

        #######################################判断
        for each_groundingdino_word in final:
            if each_groundingdino_word not in you_branch_total:
                final_groundingdino_results.append(each_groundingdino_word)

        #sample['ram_plus_nouns_groundingdino_update'] = final_groundingdino_results
        sample['YOLO11_x_nouns_update'] = final_groundingdino_results

        return sample




