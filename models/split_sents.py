from typing import  Dict
import spacy
import openai
import time
import torch
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer


class PreProcessor:
    def __init__(self, args):
        self.args = args
        self.nlp = spacy.load('en_core_web_lg')
    
    def get_split_sents(self, passage):
        doc = self.nlp(passage)        ###将文档分割成句子
        split_sents = list(doc.sents)
        split_sents = [sent.text.strip() for sent in split_sents]  ##返回一个包含分割后句子文本的列表
        return split_sents
    
    def generate_sentences(self, sample: Dict, pipeline):
        
        split_sents = self.get_split_sents(sample['input_desc'])   ##将输入的一大段描述，分割为句子列表
        
        sample['split_sents'] = split_sents

        return sample




