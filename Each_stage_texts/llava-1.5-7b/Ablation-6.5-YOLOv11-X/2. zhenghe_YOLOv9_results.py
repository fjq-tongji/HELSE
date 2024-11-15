import json

with open('./Ours_llava_7b_entity_captions_update_6_4.json', 'r', encoding='utf-8') as f:
    results_1 = json.load(f)

with open('./YOLO11_x_results_gai.json', 'r', encoding='utf-8') as f:
    Tag2text_results = json.load(f)

final = []
for k in results_1:
    new_dict = {}
    find_img = k['img_path']
    for j in Tag2text_results:
        if j['img_path'] == find_img:
            new_dict['img_path'] = k['img_path']
            new_dict['input_desc'] = k['input_desc']
            new_dict['split_sents'] = k['split_sents']
            new_dict['named_entity'] = k['named_entity']
            new_dict['entity_answers_blip2'] = k['entity_answers_blip2']
            new_dict['entity_answers_instructblip'] = k['entity_answers_instructblip']
            new_dict['named_entity_blip2_instructblip_update'] = k['named_entity_blip2_instructblip_update']
            new_dict['named_entity_split_sents_update'] = k['named_entity_split_sents_update']
            new_dict['YOLO11_x_results'] = j['YOLO11_x_results']
            final.append(new_dict)
            break

with open('Ours_llava_7b_entity_captions_update_6_4_new.json', 'w') as f:
    json.dump(final, f, indent=4)




