import os
import torch
from typing import Dict

from PIL import Image
from transformers import StoppingCriteriaList


def get_answer(processor, model, img, qs):
    inputs = processor(img, qs, return_tensors="pt").to("cuda:0", torch.float32)

    generated_ids = model.generate(**inputs)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    return generated_text.strip()


def get_all_answers_insblip_vicuna(processor, model, word, input_img_path):
    prompt_moban = 'Is there a {} in the image? Please answer only with yes or no.'
    qs = prompt_moban.format(word)
    img = Image.open(input_img_path).convert('RGB')
    answer = get_answer(processor, model, img, qs)

    return answer


###########################################################
class Update_entity:
    def __init__(self, args):
        self.args = args

    def filter_entity(self, processor_insblip_vicuna, model_insblip_vicuna, sample: Dict, pipeline):
        img_name = sample['img_path']
        total_entity = sample['named_entity']
        entity_answers_blip2 = sample['entity_answers_blip2']
        entity_answers_instructblip = sample['entity_answers_instructblip']
        entity_update = []
        for k in range(len(total_entity)):
            entity_update_line = []
            each_entity = total_entity[k]
            entity_blip2_ans = entity_answers_blip2[k]
            entity_instructblip_ans = entity_answers_instructblip[k]
            if '.' in each_entity:                               ####man.building.wheel
                each_entity_lst = each_entity.split('.')
                entity_blip2_ans_lst = entity_blip2_ans.split('.')
                entity_instructblip_ans_lst = entity_instructblip_ans.split('.')
                for j in range(len(each_entity_lst)):
                    if ('yes' in entity_blip2_ans_lst[j].lower()) and ('yes' in entity_instructblip_ans_lst[j].lower()):
                        entity_update_line.append(each_entity_lst[j])
                    elif entity_blip2_ans_lst[j].lower() != entity_instructblip_ans_lst[j].lower():
                        ans_3 = get_all_answers_insblip_vicuna(processor_insblip_vicuna, model_insblip_vicuna, each_entity_lst[j], img_name)
                        print(ans_3)
                        if 'yes' in ans_3.lower():
                            entity_update_line.append(each_entity_lst[j])
                if len(entity_update_line) == 0:
                    entity_update.append('No this word')
                else:
                    entity_update_line_result = '.'.join(entity_update_line)
                    entity_update.append(entity_update_line_result)


            elif '.' not in each_entity and 'None' not in each_entity:            ###car
                if ('yes' in entity_blip2_ans.lower()) and ('yes' in entity_instructblip_ans.lower()):
                    entity_update.append(each_entity)
                elif entity_blip2_ans.lower() != entity_instructblip_ans.lower():
                    ans_3 = get_all_answers_insblip_vicuna(processor_insblip_vicuna, model_insblip_vicuna, each_entity, img_name)
                    print(ans_3)
                    if 'yes' in ans_3.lower():
                        entity_update.append(each_entity)
                    else:
                        entity_update.append('No this word')
                else:
                    entity_update.append('No this word')

            elif 'None' in each_entity:                                           ###None
                entity_update.append(each_entity)

        sample['named_entity_blip2_instructblip_update'] = entity_update

        return sample





