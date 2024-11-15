import json

final = []
input_json_stage3 = './Ours_llava_7b_entity_update_3_4.json'                    ###模块3输出的结果,有右分支最后的实体。涉及到左分支ram的都用不了，是基于ram0.6的结果
input_json_stage5 = '../Ablation2-m125/Ours_llava_7b_groundingdino_captions_5_4.json'     ###只有ram_plus_nouns和ram_plus_nouns_captions
input_json_stage4_groundingdino = '../../Ours_llava_7b_ram_0.5_groundingdino_4_4.json'   ###这里的ram_plus_nouns_groundingdino是能用的
output_json = './Ours_llava_7b_groundingdino_captions_5_4_Ablation5.1.json'


with open(input_json_stage3, 'r', encoding='utf-8') as f3:
    stage_3 = json.load(f3)

with open(input_json_stage5, 'r', encoding='utf-8') as f5:
    stage_5 = json.load(f5)

with open(input_json_stage4_groundingdino, 'r', encoding='utf-8') as f5:
    input_json_stage4_groundingdino = json.load(f5)

final = []
for k in range(len(stage_3)):
    new_dict = {}
    new_dict['img_path'] = stage_3[k]['img_path']
    new_dict['input_desc'] = stage_3[k]['input_desc']
    new_dict['named_entity'] = stage_3[k]['named_entity']
    new_dict['ram_plus_nouns'] = input_json_stage4_groundingdino[k]['ram_plus_nouns']
    new_dict['ram_plus_nouns_groundingdino'] = input_json_stage4_groundingdino[k]['ram_plus_nouns_groundingdino']
    new_dict['entity_answers_blip2'] = stage_3[k]['entity_answers_blip2']
    new_dict['entity_answers_instructblip'] = stage_3[k]['entity_answers_instructblip']
    new_dict['named_entity_blip2_instructblip_update'] = stage_3[k]['named_entity_blip2_instructblip_update']
    new_dict['named_entity_split_sents_update'] = stage_3[k]['named_entity_split_sents_update']
    new_dict['named_entity_blip2_instructblip_update_5.1'] = stage_3[k]['named_entity_blip2_instructblip_update_5.1']

    ################################1.找到ram_plus_nouns_groundingdino中每一个名词对应的句子
    ram_plus_nouns_groundingdino_captions = []
    all_ram_plus_nouns_captions = stage_5[k]['ram_plus_nouns_captions']
    all_ram_plus_nouns = input_json_stage4_groundingdino[k]["ram_plus_nouns"]
    all_ram_plus_nouns_after_groundingdino = input_json_stage4_groundingdino[k]['ram_plus_nouns_groundingdino']
    for n in range(len(all_ram_plus_nouns_after_groundingdino)):
        each_word = all_ram_plus_nouns_after_groundingdino[n]
        for kk in range(len(all_ram_plus_nouns)):
            if each_word == all_ram_plus_nouns[kk]:
                ram_plus_nouns_groundingdino_captions.append(all_ram_plus_nouns_captions[kk])
                break
    new_dict['ram_plus_nouns_groundingdino_captions'] = ram_plus_nouns_groundingdino_captions
    ################################

    ################################2.模块3输出的总的词
    module_5_3_zong_words_yuan = stage_3[k]['named_entity_blip2_instructblip_update_5.1']
    module_5_3_zong_words = []
    for m in range(len(module_5_3_zong_words_yuan)):
        if 'No this word' in module_5_3_zong_words_yuan[m]:
            continue
        elif '.' not in module_5_3_zong_words_yuan[m]:
            module_5_3_zong_words.append(module_5_3_zong_words_yuan[m])
        elif '.' in module_5_3_zong_words_yuan[m]:
            module_5_3_zong_words.extend(module_5_3_zong_words_yuan[m].split('.'))
    ################################

    ################################3.利用模块3总的词对groundingdino的词语进行过滤
    final_captions_left = []
    for p in range(len(all_ram_plus_nouns_after_groundingdino)):
        each_word_ = all_ram_plus_nouns_after_groundingdino[p]
        if each_word_ not in module_5_3_zong_words:
            final_captions_left.append(ram_plus_nouns_groundingdino_captions[p])
    new_dict['Module_5_final_captions'] = final_captions_left

    final.append(new_dict)



with open(output_json, 'w', encoding='utf-8') as f:
    json.dump(final, f, indent=4, ensure_ascii=False)



