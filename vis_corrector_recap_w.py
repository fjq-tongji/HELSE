from models.split_sents import PreProcessor
from models.entity_extractor import EntityExtractor
from models.blip2_flant5 import Answer
from models.instructblip_flant5 import Answer_Ins
from models.update_entity import Update_entity
from models.groundingdino import Detector
from models.groundingdino_words_you_update import Groundingdino_words_you_update
from models.groundingdino_write_captions import Groundingdino_write_captions
from models.update_entity_sents import Update_entity_captions


from tqdm import tqdm
from typing import List, Dict
import time
import transformers
import torch


class Corrector:
    def __init__(self, args) -> None:
        
        self.split_sents = PreProcessor(args)
        self.named_entity = EntityExtractor(args)
        self.blip2 = Answer(args)
        self.instructblip = Answer_Ins(args)
        self.entity_update = Update_entity(args)
        self.groundingdino = Detector(args)
        self.groundingdino_update = Groundingdino_words_you_update(args)
        self.groundingdino_captions = Groundingdino_write_captions(args)
        self.rewrite_entity_sents = Update_entity_captions(args)

        print("Finish loading models.")

    
    def correct(self, pipeline, processor_blip, model_blip, processor_instructblip, model_instructblip,
                processor_insblip_vicuna, model_insblip_vicuna, sample: Dict):

        sample = self.split_sents.generate_sentences(sample, pipeline)
        print('------------1-----------')
        sample = self.named_entity.extract_entity(sample, pipeline)
        print('------------2-----------')
        sample = self.blip2.generate_answers(processor_blip, model_blip, sample)
        print('------------3------------')
        sample = self.instructblip.generate_answers(processor_instructblip, model_instructblip, sample)
        print('------------3------------')
        sample = self.entity_update.filter_entity(processor_insblip_vicuna, model_insblip_vicuna, sample, pipeline)
        print('------------3------------')
        sample = self.groundingdino.detect_objects(sample, pipeline)
        print('------------4------------')
        sample = self.groundingdino_update.groundingdino_words_update(sample, pipeline)
        print('------------4------------')

        sample = self.groundingdino_captions.generate_captions(processor_blip, model_blip, sample)
        print('------------5------------')
        sample = self.rewrite_entity_sents.rewrite_entity_captions(sample, pipeline)
        # print('------------6------------')



        return sample




