import os
import torch
from PIL import Image
from typing import Dict


def get_answer(processor, model, img, qs):
    inputs = processor(img, qs, return_tensors="pt").to("cuda:0", torch.float32)

    generated_ids = model.generate(**inputs)
    generated_text = processor.decode(generated_ids[0], skip_special_tokens=True)
    return generated_text.strip()


def get_all_answers(processor, model, qs, input_img_path):
    img = Image.open(input_img_path).convert('RGB')
    answer = get_answer(processor, model, img, qs)

    return answer

class Groundingdino_write_captions:
    def __init__(self, args):
        self.args = args
    

    def generate_captions(self, processor_blip, model_blip, sample: Dict):
        qs = 'Describe the {} in the image with only one sentence.'
        total_groundingdino_words = sample['ram_plus_nouns_groundingdino_update']
        final_captions = []
        if len(total_groundingdino_words) > 0:
            for each_word in total_groundingdino_words:
                qs_ = qs.format(each_word)
                caption_ = get_all_answers(processor_blip, model_blip, qs_, sample['img_path'])
                final_captions.append(caption_)

        sample['ram_plus_nouns_groundingdino_captions'] = final_captions

        return sample



