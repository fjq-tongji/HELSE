CODA_desc.rar and nuScenes_desc.rar are the created datasets.

Since we have four GPUs, the code of each stage is divides into four sub-files. \n
"Sentence Split" corresponds to the codes of inference_split_sents.py. 
"Key Entity Extraction" corresponds to the codes of inference_named_entity_1_x.py.
"Entity Filtering" corresponds to the codes of inference_blip2_3_x.py, inference_instructblip_3_x.py, and inference_entity_update_3_x.py.
"Hallucination Correction" corresponds to the codes of inference_entity_captions_update_6_x.py.
"Object Detection" corresponds to the codes of 1. inference_ram_plus_CODA.py in the "RAM++ Codes" folder, and inference_groundingdino_4_x.py.
"Object Description" corresponds to the codes of inference_groundingdino_write_captions_5_x.py.

