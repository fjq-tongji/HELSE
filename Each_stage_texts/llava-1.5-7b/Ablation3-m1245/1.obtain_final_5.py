import json

final = []
input_json = './Ours_llava_7b_groundingdino_captions_5_3.json'        ###ram+所有名词对应的句子
input_json_2 = './Ours_llava_7b_ram_0.5_groundingdino_4_3.json'       ###经过groundingdino后剩余的名词
output_json = './Ours_llava_7b_groundingdino_captions_5_3_new.json'


with open(input_json, 'r', encoding='utf-8') as f:
    file_ram_plus_nouns_all_captions = json.load(f)

with open(input_json_2, 'r', encoding='utf-8') as f2:
    file_ram_plus_nouns_groundingdino = json.load(f2)

final = []
for k in range(len(file_ram_plus_nouns_all_captions)):
    each_img_dict = file_ram_plus_nouns_all_captions[k]
    each_img_dict_groundingdino_lst = file_ram_plus_nouns_groundingdino[k]
    new_dict = {}
    new_dict['img_path'] = each_img_dict['img_path']
    new_dict['input_desc'] = each_img_dict['input_desc']
    new_dict['split_sents'] = each_img_dict['split_sents']
    new_dict['named_entity'] = each_img_dict['named_entity']
    new_dict['ram_plus_nouns'] = each_img_dict['ram_plus_nouns']                               ##所有名词
    new_dict['ram_plus_nouns_captions'] = each_img_dict['ram_plus_nouns_captions']             ##所有名词对应的句子
    new_dict['ram_plus_nouns_groundingdino'] = each_img_dict_groundingdino_lst['ram_plus_nouns_groundingdino']      ##一部分名词

    all_ram_plus_nouns_captions_lst = new_dict['ram_plus_nouns_captions']

    final_groundingdino_captions = []
    for m in range(len(new_dict['ram_plus_nouns'])):
        each_word = new_dict['ram_plus_nouns'][m]
        if each_word in new_dict['ram_plus_nouns_groundingdino']:
            final_groundingdino_captions.append(all_ram_plus_nouns_captions_lst[m])
    new_dict['ram_plus_nouns_groundingdino_captions'] = final_groundingdino_captions

    final.append(new_dict)

with open(output_json, 'w', encoding='utf-8') as f:
    json.dump(final, f, indent=4, ensure_ascii=False)








