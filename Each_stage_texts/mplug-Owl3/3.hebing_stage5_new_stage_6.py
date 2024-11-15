import json

file_stage5_new = './Ours_mplug_owl3_groundingdino_captions_5_1.json'
file_stage6 = './Ours_mplug_owl3_entity_captions_update_6_1.json'
output_json = './Ours_mplug_owl3_entity_captions_update_6_1_new.json'


with open(file_stage5_new, 'r', encoding='utf-8') as f:
    stage5_new = json.load(f)
with open(file_stage6, 'r', encoding='utf-8') as f:
    stage6 = json.load(f)

final = []
for kk in range(len(stage6)):
    new_dict = {}
    new_dict['img_path'] = stage5_new[kk]['img_path']
    new_dict['input_desc'] = stage5_new[kk]['input_desc']
    new_dict['split_sents'] = stage5_new[kk]['split_sents']
    new_dict['named_entity'] = stage5_new[kk]['named_entity']
    new_dict['entity_answers_blip2'] = stage5_new[kk]['entity_answers_blip2']
    new_dict['entity_answers_instructblip'] = stage5_new[kk]['entity_answers_instructblip']
    new_dict['named_entity_blip2_instructblip_update'] = stage5_new[kk]['named_entity_blip2_instructblip_update']
    new_dict['ram_plus_nouns'] = stage5_new[kk]['ram_plus_nouns']
    new_dict['ram_plus_nouns_groundingdino'] = stage5_new[kk]['ram_plus_nouns_groundingdino']
    new_dict['ram_plus_nouns_groundingdino_update'] = stage5_new[kk]['ram_plus_nouns_groundingdino_update']
    new_dict['ram_plus_nouns_groundingdino_captions'] = stage5_new[kk]['ram_plus_nouns_groundingdino_captions']
    new_dict['named_entity_split_sents_update'] = stage6[kk]['named_entity_split_sents_update']

    final.append(new_dict)

with open(output_json, 'w', encoding='utf-8') as f:
    json.dump(final, f, indent=4, ensure_ascii=False)





