import os
#os.environ["CUDA_VISIBLE_DEVICES"]="6"
import torch
from PIL import Image
from transformers import Blip2Processor, Blip2ForConditionalGeneration
#from transformers import AutoProcessor, AutoModelForSeq2SeqLM
from typing import Dict


def get_answer(processor, model, img, qs):
    inputs = processor(img, qs, return_tensors="pt").to("cuda:0", torch.float32)

    generated_ids = model.generate(**inputs)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    # generated_text = processor.decode(generated_ids[0], skip_special_tokens=True)
    return generated_text.strip()

# def get_all_answers(processor, model, entity_list, qs, ent_info, input_img_path, cur_answers):
#     # This should return a dict. Since a question may correspond to multiple instances of a same kind of object.
#     # case 1: involve multiple entities or 'where' type question: use the whole img.
#     if len(entity_list)>1 or 'where' in qs.lower() or any([ent not in ent_info for ent in entity_list]):
#         img = Image.open(input_img_path).convert('RGB')
#         answer = get_answer(processor, model, img, qs)
#         cur_answers.setdefault('overall', [])   # use a special category 'overall' to denote answers that involve multiple objects.
#         cur_answers['overall'].append((qs, answer))
#     else:
#         entity = entity_list[0]
#         # case 2: single entity : single/multiple instances.
#         for idx, img_path in enumerate(ent_info[entity]['crop_path']):
#             img = Image.open(img_path).convert('RGB')
#             answer = get_answer(processor, model, img, qs)
#             cur_answers.setdefault(entity, [])
#             if idx + 1 > len(cur_answers[entity]):
#                 cur_answers[entity].append([])
#             cur_answers[entity][idx].append((qs, answer))
#     return cur_answers


def get_all_answers(processor, model, qs, input_img_path):
    img = Image.open(input_img_path).convert('RGB')
    answer = get_answer(processor, model, img, qs)

    return answer

class Answer_Ins:
    '''
        Input: 
            'generated_questions': a list of 2-ele list, each [qs(str), involved entities(str)]
            'entity_info': A dict recording the global object information.
            key: obj name. (obj1 | obj2 | obj3)
            value:
                {
                    total_count: detected counts of that obj.
                    
                    crop_path: a list of str, denoting the path to cached intermediate file, i.e., cropped out region of that obj.
                        Note: if total_count > 1, may use the whole image in the following steps.
                        
                    bbox: each [x1, y1, x2, y2], normalized coordinates of left-top and right-bottom corners of bounding boxes.
                }
        Output:
            'generated_answers': An 1-d list of dict. Each dict in the list contains all the (qs, ans) tuple for each object instance.
                                {
                                    overall: [(qs, answer), ...]
                                    entity:  [
                                                [(qs, answer), ...]   (for instance 1 of this type of entity)
                                                    ...
                                             ]
                                }
    '''
    
    def __init__(self, args):
        self.args = args
    

    def generate_answers(self, processor_blip, model_blip, sample: Dict):
        #################根据实体，构建所有的问题
        qs_zong = []
        qs = 'Is there a {} in the image? Please answer only with yes or no.'
        total_entity = sample['named_entity']
        for each_entity in total_entity:       #### man.tires
            if 'None' in each_entity:
                qs_zong.append([])
                continue
            elif '.' in each_entity:
                each_entity_lst = each_entity.split('.')        #### [man,tires]
                qs_line = []
                for k in each_entity_lst:
                    qs_ = qs.format(k)
                    qs_line.append(qs_)
                qs_zong.append(qs_line)
            else:                             ### 说明这一行只有一个实体
                qs_ = qs.format(each_entity)
                qs_zong.append([qs_])
        print(qs_zong)

        #################依次回答每一行对应的所有问题
        all_answers = []
        for each_qs in qs_zong:
            if len(each_qs) == 0:
                all_answers.append([])
                continue
            else:
                each_line_answer = []
                for k in range(len(each_qs)):
                    each_sub_qs = each_qs[k]
                    cur_answer = get_all_answers(processor_blip, model_blip, each_sub_qs, sample['img_path'])   ##yes/no
                    each_line_answer.append(cur_answer)
                all_answers.append(each_line_answer)
        print(all_answers)

        #################将答案进行整合,以yes.yes.no的格式保存
        final_answers = []
        for each_answer in all_answers:
            if len(each_answer) == 0:
                final_answers.append("None")
                continue
            else:
                final_answers.append('.'.join(each_answer))
                
        sample['entity_answers_instructblip'] = final_answers

        return sample
    





