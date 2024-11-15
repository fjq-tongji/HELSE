import json

final = []
input_json = './Ours_llava_7b_entity_captions_update_6_4.json'
output_json = './Ours_llava_7b_entity_captions_update_6_4_new.json'


with open(input_json, 'r', encoding='utf-8') as f:
    stage_3 = json.load(f)

for k in range(len(stage_3)):
    new_dict = {}
    new_dict['img_path'] = stage_3[k]['img_path']
    new_dict['input_desc'] = stage_3[k]['input_desc']
    new_dict['split_sents'] = stage_3[k]['split_sents']
    new_dict['named_entity'] = stage_3[k]['named_entity']
    new_dict['entity_answers_blip2'] = stage_3[k]['entity_answers_blip2']
    new_dict['entity_answers_instructblip'] = stage_3[k]['entity_answers_instructblip']
    new_dict['named_entity_blip2_instructblip_update'] = stage_3[k]['named_entity_blip2_instructblip_update']
    new_dict['named_entity_split_sents_update'] = stage_3[k]['named_entity_split_sents_update']

    final.append(new_dict)



with open(output_json, 'w', encoding='utf-8') as f:
    json.dump(final, f, indent=4, ensure_ascii=False)



