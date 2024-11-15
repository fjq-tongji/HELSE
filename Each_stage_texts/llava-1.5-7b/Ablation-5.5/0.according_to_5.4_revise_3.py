import json

final = []
input_json_stage3 = './Ours_llava_7b_entity_update_3_3.json'         ###模块3输出的结果
input_json_stage4 = '../Ablation-5.4/Ours_llava_7b_entity_captions_update_6_3_new.json'
output_json = './Ours_llava_7b_entity_update_3_3_new.json'

with open(input_json_stage3, 'r', encoding='utf-8') as f3:
    stage_5_5 = json.load(f3)

with open(input_json_stage4, 'r', encoding='utf-8') as f5:
    stage_5_4 = json.load(f5)

final = []
for k in range(len(stage_5_5)):
    new_dict = {}
    new_dict['named_entity_blip2_instructblip_update_5.4'] = stage_5_4[k]['named_entity_blip2_instructblip_update_5.4']
    new_dict['named_entity_split_sents_update_5.4'] = stage_5_4[k]['named_entity_split_sents_update_5.4']
    B = stage_5_5[k].copy()
    B.update(new_dict)
    final.append(B)


with open(output_json, 'w', encoding='utf-8') as f:
    json.dump(final, f, indent=4, ensure_ascii=False)



