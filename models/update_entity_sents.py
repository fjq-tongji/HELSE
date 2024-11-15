import os
import torch
from typing import Dict



PROMPT_TEMPLATE='''Given a sentence and two entities, you are required to correct the sentence output the refined sentence in a fluent and natural style, following these rules:
1. "Entity_1" information that some entity words;
   "Entity_2" information that some updated entity words. In this information, different entities are separated with a dot. 
   "Sentence" information that a sentence that needs to be updated.
2. If a word appears in "Entity_1" but not in "Entity_2", remove the relevant description of this word in "Sentence".
3. Note that the singular and plural forms of a noun are considered to be the same word, for example: person and people can be seen as same words.


Examples:
Entity_1:
truck.crane

Entity_2:
truck

Sentence:
The image depicts a busy city street with a large truck driving down the road, carrying a crane on its back.

Output:
The image depicts a busy city street with a large truck driving down the road.

--------------------------------------------

Entity_1:
person.traffic_light.vehicles

Entity_2:
vehicles

Sentence:
In addition to the vehicles and traffic lights, there are two people visible in the scene, one near the center and the other towards the right side of the image.

Output:
There are some vehicles in the image.

--------------------------------------------

Entity_1:
{Entity_1}

Entity_2:
{Entity_2}

Sentence:
{Sentence}

Output_ours:'''



def update_sent(entity_words_yuan, entity_words_update, split_sents_yuan, pipeline, max_tokens: int=100):
    # query = 'Please describe this image with one sentence.'
    content = PROMPT_TEMPLATE.format(Entity_1=entity_words_yuan, Entity_2=entity_words_update, Sentence=split_sents_yuan
                                     )
    generated_text = pipeline(content, pad_token_id=pipeline.tokenizer.eos_token_id,
                              max_new_tokens=max_tokens)[0]['generated_text']
    output_start = generated_text.find("Output_ours:") + len("Output_ours:")
    generated_text_1 = generated_text[output_start:].strip()
    output_end = generated_text_1.find("\n")
    generated_text = generated_text_1[:output_end].strip()

    return generated_text






class Update_entity_captions:
    def __init__(self, args):
        self.args = args


    def rewrite_entity_captions(self, sample: Dict, pipeline):
        entity_words_yuan = sample['named_entity']
        entity_words_update = sample['named_entity_blip2_instructblip_update']
        split_sents_yuan = sample['split_sents']
        final_sents = []
        for k in range(len(entity_words_yuan)):
            if 'No this word' in entity_words_update[k]:
                continue
            elif entity_words_yuan[k] == entity_words_update[k]:
                final_sents.append(split_sents_yuan[k])
            else:
                new_sent = update_sent(entity_words_yuan[k], entity_words_update[k], split_sents_yuan[k], pipeline)
                final_sents.append(new_sent)


        sample['named_entity_split_sents_update'] = final_sents

        return sample





