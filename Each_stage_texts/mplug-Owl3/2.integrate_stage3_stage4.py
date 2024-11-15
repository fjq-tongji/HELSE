import json

with open('./Ours_mplug_owl3_entity_update_3_4.json', 'r', encoding='utf-8') as f:    ##有blip2、insblip、insblip-vicuna过滤后的结果
    f_1 = json.load(f)

with open('./generic_ram_dicts_4.json', 'r', encoding='utf-8') as f:     ##有groundingdino的结果
    f_2 = json.load(f)

final = []
for k in range(len(f_2)):
    new_dict = {}
    new_dict['img_path'] = f_1[k]['img_path']
    new_dict['input_desc'] = f_1[k]['input_desc']
    new_dict['split_sents'] = f_1[k]['split_sents']
    new_dict['named_entity'] = f_1[k]['named_entity']
    new_dict['entity_answers_blip2'] = f_1[k]['entity_answers_blip2']
    new_dict['entity_answers_instructblip'] = f_1[k]['entity_answers_instructblip']
    new_dict['named_entity_blip2_instructblip_update'] = f_1[k]['named_entity_blip2_instructblip_update']

    new_dict['ram_plus_nouns'] = f_2[k]['ram_plus_nouns']
    new_dict['ram_plus_nouns_groundingdino'] = f_2[k]['ram_plus_nouns_groundingdino']

    final.append(new_dict)


with open('./Ours_mplug_owl3_ram_0.5_groundingdino_integrate_4_4.json', 'w', encoding='utf-8') as f:
    json.dump(final, f, indent=4, ensure_ascii=False)












