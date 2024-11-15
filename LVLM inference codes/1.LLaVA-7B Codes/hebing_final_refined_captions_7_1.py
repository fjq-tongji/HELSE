import json

final = []
input_json = './Each_stage_texts/Ours_llava_7b_groundingdino_captions_5_3.json'
output_json = './Each_stage_texts/Ours_llava_7b_refined_desc_7_3.json'


with open(input_json, 'r', encoding='utf-8') as f:
    stage_6 = json.load(f)

for k in range(len(stage_6)):
    new_dict = {}
    new_dict['img_path'] = stage_6[k]['img_path']
    new_dict['input_desc'] = stage_6[k]['input_desc']
    # new_dict['split_sents'] = stage_6[k]['split_sents']
    # new_dict['named_entity'] = stage_6[k]['named_entity']
    # new_dict['ram_plus_nouns'] = stage_6[k]['ram_plus_nouns']
    # new_dict['ram_plus_nouns_groundingdino'] = stage_6[k]['ram_plus_nouns_groundingdino']
    # new_dict['entity_answers_blip2'] = stage_6[k]['entity_answers_blip2']
    # new_dict['entity_answers_instructblip'] = stage_6[k]['entity_answers_instructblip']
    # new_dict['named_entity_blip2_instructblip_update'] = stage_6[k]['named_entity_blip2_instructblip_update']
    # new_dict['ram_plus_nouns_groundingdino_update'] = stage_6[k]['ram_plus_nouns_groundingdino_update']
    # new_dict['ram_plus_nouns_groundingdino_captions'] = stage_6[k]['ram_plus_nouns_groundingdino_captions']
    # new_dict['named_entity_split_sents_update'] = stage_6[k]['named_entity_split_sents_update']


    ######################## 对阶段6的输出整合成一段话
    refined_passages_stage_6 = ' '.join(stage_6[k]['named_entity_split_sents_update'])   ###阶段6得到的一段话str

    ######################## 对阶段5的输出整合成一段话：a cement mixer is driving on the bridge, a cement mixer is driving on the highway.
    zhenghe_stage5 = []
    for each_sent in stage_6[k]['ram_plus_nouns_groundingdino_captions']:
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



