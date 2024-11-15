from typing import  Dict
from tqdm import tqdm
import openai
import time
import spacy
import os
import torch
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

# 设置环境变量
#os.environ["CUDA_LAUNCH_BLOCKING"] = "1"


PROMPT_TEMPLATE='''Given a sentence, extract the entities within the sentence for me. 
Extract the common objects and summarize them as general categories without repetition, merge essentially similar objects.
Avoid extracting abstract or non-specific entities. 
Extract entity in the singular form. Output all the extracted types of items in one line and separate each object type with a period. If there is nothing to output, then output a single "None".

Examples:
Sentence:
The image depicts a man laying on the ground next to a motorcycle, which appears to have been involved in a crash.

Output:
man.motorcycle

Sentence:
There are a few people around, including one person standing close to the motorcyclist and another person further away.

Output:
person.motorcyclist

Sentence:
{sentence}

Output_ours:'''

def get_res(sent: str, pipeline, max_tokens: int=20):
    content = PROMPT_TEMPLATE.format(sentence=sent)

    generated_text = pipeline(content, pad_token_id=pipeline.tokenizer.eos_token_id,
                              max_new_tokens=max_tokens)[0]['generated_text']
    output_start = generated_text.find("Output_ours:") + len("Output_ours:")
    generated_text_1 = generated_text[output_start:].strip()
    output_end = generated_text_1.find("\n")
    generated_text = generated_text_1[:output_end].strip()

    return generated_text

def extract_entities(text: str):
    nlp = spacy.load('en_core_web_lg')
    doc = nlp(text)
    entities = [token.text for token in doc if token.pos_ == 'NOUN']
    return '.'.join(set(entities)) if entities else 'None'




class EntityExtractor:
    def __init__(self, args):
        self.args = args
    
    def extract_entity(self, sample: Dict, pipeline):
        extracted_entities = []
        for sent in sample['split_sents']:
            entity_str = get_res(sent, pipeline)
            extracted_entities.append(entity_str)

        sample['named_entity'] = extracted_entities
        
        return sample


