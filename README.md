<div style="text-align: center;">
  <h1>Hallucination Elimination and Semantic Enhancement Framework for Vision-Language Models in Traffic Scenarios</h1>
</div>

![Logo](images/label_coda+nuscenes_13.jpg)

If you have any question, please feel free to email fanjq@tongji.edu.cn.

## :fire: News
- This paper is submitted to IEEE Transactions on Intelligent Transportation Systems.
- Read our arXiv Paper [https://arxiv.org/abs/2412.07518]
- CODA_desc.rar and nuScenes_desc.rar are the created datasets.  
- [Watch the video demo](https://github.com/fjq-tongji/HCOENet/releases/download/demo/Video.Demo.mp4)

## :book: Model
![Logo](images/overall39.jpg)

## :star: Installation



## :star: Inference
1. Download the traffic dataset from CODA website (https://coda-dataset.github.io);
2. Generate question-answer pair using POPE code (./POPE codes/CODA2022/CODA2022_pope_random.json,./POPE codes/CODA2022/CODA2022_pope_popular.json,./POPE codes/CODA2022/CODA2022_pope_adversarial.json)
3. Generate initial response for each image using specific LVLM, such as LLaVA-1.5, mPLUG-Owl.
4. Generate refined response using HCOENet framework:  
   a. python inference_split_sents.py    
   b. python inference_named_entity.py  
   c. python inference_blip2_3.py  
   d. python inference_instructblip_3.py  
   e. python inference_entity_update_3.py  
   f. python inference_groundingdino_4.py  
   g. python inference_groundingdino_words_update_4.py  
   h. python inference_groundingdino_write_captions_5.py  
   i. python inference_entity_captions_update_6.py
5. Evaluate the model under POPE benchmark.
6. Generate more refined descriptions using nuScenes dataset.   

## :trophy: Results
### Ablation studies
Table 1. Ablation studies of the effectiveness of each stage in the HCOENet. Stage1 refers the sentence split and key entity extraction, stage2 refers the entity cross-checking, stage3 refers the hallucination correction, stage4 refers the critical-object identification, stage5 refers the object description, and stage6 refers integrating descriptions from two frameworks. (\%)  
![Logo](images/Tab_ablation1.jpg) 
### Quantitative results  
Table 2. Evaluation results of five LVLMs on the POPE benchmark under three negative sampling settings. (\%)  
![Logo](images/Tab1.jpg)  
Table 3. Comparison results between different mPLUG-Owl models on the POPE benchmark. (\%)  
![Logo](images/Tab2.jpg)  
Table 4. Comparison with the GPT-4o model on the POPE benchmark. B denotes billion and T denotes trillion. (\%)  
![Logo](images/Tab3.jpg)
### Qualitative results  
![Logo](images/campus_img.jpg)  

## :sunflower: Acknowledgement
This repository benefits from the following codes. Thanks for their awesome works.
- [LLaVA](https://github.com/haotian-liu/LLaVA)
- [mPLUG-Owl](https://github.com/X-PLUG/mPLUG-Owl)
- [MiniGPT-4](https://github.com/Vision-CAIR/MiniGPT-4)
- [InternVL](https://github.com/OpenGVLab/InternVL)
- [BLIP-2](https://huggingface.co/Salesforce/blip2-flan-t5-xxl)
- [InstructBLIP](https://huggingface.co/Salesforce/instructblip-flan-t5-xxl)(https://huggingface.co/Salesforce/instructblip-vicuna-13b)
- [Woodpecker](https://github.com/BradyFU/Woodpecker)
- [POPE](https://github.com/AoiDragon/POPE)
- [RAM](https://github.com/xinyu1205/recognize-anything)
- [GroundingDINO](https://github.com/IDEA-Research/GroundingDINO)

## :scroll: Citation
@article{Hallucination,  
  title={Hallucination Elimination and Semantic Enhancement Framework for Vision-Language Models in Traffic Scenarios},  
  author={Jiaqi Fan and Jianhua Wu and Hongqing Chu and Quanbo Ge and Bingzhao Gao},  
  year={2024},  
  url={https://api.semanticscholar.org/CorpusID:274610465}  
}  

