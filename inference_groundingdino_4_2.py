from vis_corrector_recap_w import Corrector
from types import SimpleNamespace
import argparse
import json
import gc
import transformers, torch, spacy, os
from tqdm import tqdm
from typing import Dict, List
from transformers import pipeline


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Code for 'ReCaption'.")
    parser.add_argument('--stage-1', default='./Each_stage_texts/MiniGPT-4/RAM_plus_results_0.3_1.json')
    parser.add_argument('--query', default='Describe this image.', type=str, help="text query for MLLM")
    parser.add_argument('--cache-dir', type=str, default='./cache_dir')
    parser.add_argument('--detector-config',
                        default='/home/fjq/MLLMs/Woodpecker/groundingdino/config/GroundingDINO_SwinB_cfg.py', type=str, help="Path to the detector config, \
                            in the form of 'path/to/GroundingDINO_SwinT_OGC.py' ")
    parser.add_argument('--detector-model', default='/data/fjq/3.VLMS/Woodpecker/groundingdino_swinb_ogc.pth', type=str,
                        help="Path to the detector checkpoint, \
                            in the form of 'path/to/groundingdino_swint_ogc.pth' ")

    args = parser.parse_args()
    
    args_dict = {
        'cache_dir': args.cache_dir,
        'detector_config': args.detector_config,
        'detector_model_path': args.detector_model,
}

    model_args = SimpleNamespace(**args_dict)
    #pipeline = transformers.pipeline(
     #       "text-generation", model='/data/lqf_llama/Meta-Llama-3-8B-Instruct',
      #      model_kwargs={"torch_dtype": torch.float32},
       #     device_map={"": 0}
        #)
    pipeline = 1

    corrector = Corrector(model_args)
    final_text = []

    ##所有的coda图片的详细描述，存到列表中
    with open(args.stage_1, 'r', encoding='utf-8') as f:
        coda_detail_captions = json.load(f)

    coda_detail_captions_correct = []
    for sample in coda_detail_captions:
        output = corrector.correct(pipeline, pipeline,pipeline,pipeline,pipeline, pipeline,pipeline, sample)
        print(output)
        coda_detail_captions_correct.append(output)
        print(len(coda_detail_captions_correct))


    with open('./Each_stage_texts/RAM_plus_results_0.3_groundingdino_1.json', 'w', encoding='utf-8') as f:
        json.dump(coda_detail_captions_correct, f, indent=4, ensure_ascii=False)




