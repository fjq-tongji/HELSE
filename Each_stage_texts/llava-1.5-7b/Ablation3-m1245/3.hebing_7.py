import json

# file_path = './Ours_llava_7b_ram_0.6_nouns_2.json'
# with open(file_path, 'r', encoding='utf-8') as f:
#     coda_detail_captions = json.load(f)
#
# lst_1 = coda_detail_captions[:2500]
# lst_2 = coda_detail_captions[2500:5000]
# lst_3 = coda_detail_captions[5000:7500]
# lst_4 = coda_detail_captions[7500:]
#
# with open('Ours_llava_7b_ram_0.6_nouns_2_1.json', 'w', encoding='utf-8') as f:
#     json.dump(lst_1, f, indent=4, ensure_ascii=False)
#
# with open('Ours_llava_7b_ram_0.6_nouns_2_2.json', 'w', encoding='utf-8') as f:
#     json.dump(lst_2, f, indent=4, ensure_ascii=False)
#
# with open('Ours_llava_7b_ram_0.6_nouns_2_3.json', 'w', encoding='utf-8') as f:
#     json.dump(lst_3, f, indent=4, ensure_ascii=False)
#
# with open('Ours_llava_7b_ram_0.6_nouns_2_4.json', 'w', encoding='utf-8') as f:
#     json.dump(lst_4, f, indent=4, ensure_ascii=False)





file_path_1 = './Ours_llava_7b_refined_desc_7_1_m1245.json'
file_path_2 = './Ours_llava_7b_refined_desc_7_2_m1245.json'
file_path_3 = './Ours_llava_7b_refined_desc_7_3_m1245.json'
file_path_4 = './Ours_llava_7b_refined_desc_7_4_m1245.json'
final_lst = []
final_path = './Ours_llava_7b_refined_desc_7_m1245.json'

with open(file_path_1, 'r', encoding='utf-8') as f:
    f_1 = json.load(f)
    final_lst.extend(f_1)
with open(file_path_2, 'r', encoding='utf-8') as f:
    f_2 = json.load(f)
    final_lst.extend(f_2)
with open(file_path_3, 'r', encoding='utf-8') as f:
    f_3 = json.load(f)
    final_lst.extend(f_3)
with open(file_path_4, 'r', encoding='utf-8') as f:
    f_4 = json.load(f)
    final_lst.extend(f_4)

# with open(final_path, 'w', encoding='utf-8') as f:
#     json.dump(final_lst, f, indent=4, ensure_ascii=False)

with open(final_path, 'w', encoding='utf-8') as f:
    for d in final_lst:
        json.dump(d, f, ensure_ascii=False)
        f.write('\n')






