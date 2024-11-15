from models.extract_noun_verb_adj import Extractor_n_v_adj
#from models.integrate_nouns_3 import Integrate_entity_nouns
from models.groundingdino import Detector

from tqdm import tqdm
from typing import List, Dict
import time
import transformers
import torch


class Corrector:
    def __init__(self, args) -> None:
        
        self.extractor_n_v_adj = Extractor_n_v_adj(args)
        #self.integrate_nouns = Integrate_entity_nouns(args)
        self.groundingdino = Detector(args)

        
        print("Finish loading models.")

    
    def correct(self, pipeline, sample: Dict):
        '''
        sample is Dict containing at least two fields:
            'input_desc': A passage that contains a description of the image.
            'input_img': Path to a local image 
        '''

        #sample = self.extractor_n_v_adj.extract_n_v_adj(sample, pipeline)
        #print('------------1-----------')
        #sample = self.integrate_nouns.integrate_entity_nouns(sample, pipeline)
        #print('------------2------------')
        sample = self.groundingdino.detect_objects(sample)
        #print('------------3------------')

        return sample




