import json

total_dict = []
total_dict_val = []
total_dict_test = []
with open('./Ours/CODA_mplug_owl3_popular_answers_ours.json', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            # 解析每一行的JSON数据
            item = json.loads(line)
            if '_val2022_' in item['image']:
                total_dict_val.append(item)
            elif '_test2022_' in item['image']:
                total_dict_test.append(item)

with open('./Ours/CODA_mplug_owl3_popular_answers_ours_val.json', 'w', encoding='utf-8') as f:
    for d in total_dict_val:
        json.dump(d, f, ensure_ascii=False)
        f.write('\n')
with open('./Ours/CODA_mplug_owl3_popular_answers_ours_test.json', 'w', encoding='utf-8') as f:
    for d in total_dict_test:
        json.dump(d, f, ensure_ascii=False)
        f.write('\n')


##########################################################################################
# total_dict = []
# total_dict_val = []
# total_dict_test = []
# with open('./CODA_mplug_owl2_adversarial_answers.json', 'r', encoding='utf-8') as f:
#     for line in f:
#         line = line.strip()
#         if line:
#             # 解析每一行的JSON数据
#             item = json.loads(line)
#             if '_val2022_' in item['image']:
#                 total_dict_val.append(item)
#             elif '_test2022_' in item['image']:
#                 total_dict_test.append(item)
#
# with open('./CODA_mplug_owl2_adversarial_answers_val.json', 'w', encoding='utf-8') as f:
#     for d in total_dict_val:
#         json.dump(d, f, ensure_ascii=False)
#         f.write('\n')
# with open('./CODA_mplug_owl2_popular_answers_test.json', 'w', encoding='utf-8') as f:
#     for d in total_dict_test:
#         json.dump(d, f, ensure_ascii=False)
#         f.write('\n')
#
#
# ##########################################################################################
# total_dict = []
# total_dict_val = []
# total_dict_test = []
# with open('./CODA_mplug_owl2_adversarial_answers.json', 'r', encoding='utf-8') as f:
#     for line in f:
#         line = line.strip()
#         if line:
#             # 解析每一行的JSON数据
#             item = json.loads(line)
#             if '_val2022_' in item['image']:
#                 total_dict_val.append(item)
#             elif '_test2022_' in item['image']:
#                 total_dict_test.append(item)
#
# with open('./CODA_mplug_owl2_adversarial_answers_val.json', 'w', encoding='utf-8') as f:
#     for d in total_dict_val:
#         json.dump(d, f, ensure_ascii=False)
#         f.write('\n')
# with open('./CODA_mplug_owl2_adversarial_answers_test.json', 'w', encoding='utf-8') as f:
#     for d in total_dict_test:
#         json.dump(d, f, ensure_ascii=False)
#         f.write('\n')
#



