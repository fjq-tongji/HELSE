import json

final = []
input_json = './Ours_llava_7b_groundingdino_captions_5_3_Ablation5.5.json'     ###模块5输出的结果
input_json_2 = './Ours_llava_7b_entity_captions_update_6_3_new.json'   ###模块6输出的结果
output_json = './Ours_llava_7b_refined_desc_7_3_m5.5.json'


with open(input_json, 'r', encoding='utf-8') as f:
    stage_55 = json.load(f)

with open(input_json_2, 'r', encoding='utf-8') as f2:
    stage_66 = json.load(f2)

for k in range(len(stage_55)):
    new_dict = {}
    new_dict['img_path'] = stage_55[k]['img_path']
    new_dict['input_desc'] = stage_55[k]['input_desc']


    ######################## 对阶段6的输出整合成一段话
    refined_passages_stage_6 = ' '.join(stage_66[k]['named_entity_split_sents_update_5.5'])   ###阶段6得到的一段话str

    ######################## 对阶段5的输出整合成一段话：a cement mixer is driving on the bridge, a cement mixer is driving on the highway.
    zhenghe_stage5 = []
    for each_sent in stage_55[k]['Module_5_final_captions']:
        if not each_sent[0].islower():
            each_sent = each_sent[0].lower() + each_sent[1:]
        if not each_sent.endswith(','):
            each_sent += ','
        zhenghe_stage5.append(each_sent)
    refined_passages_stage_5 = ' '.join(zhenghe_stage5)                                  ###阶段5得到的一段话str
    refined_passages_stage_5 = refined_passages_stage_5[:-1] + '.'
    ########################################################################

    ######################## 对阶段6和阶段5的一段话进行合并
    refined_passages_final = ''
    refined_passages_final += refined_passages_stage_6
    refined_passages_final += ' '
    refined_passages_final += '\n\n '
    refined_passages_final += 'Some additional information includes: '
    refined_passages_final += refined_passages_stage_5      ###阶段6和阶段5合并后的一段话str

    ######################## 合并后的新的段落
    new_dict['refined_desc'] = refined_passages_final

    final.append(new_dict)



with open(output_json, 'w', encoding='utf-8') as f:
    json.dump(final, f, indent=4, ensure_ascii=False)



