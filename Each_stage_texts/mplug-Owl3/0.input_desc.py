import json

input_json = './CODA_mPLUG_Owl3_detail_captions.json'
output_json = './CODA_mPLUG_Owl3_detail_captions_new.json'


final = []
with open(input_json, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            # 解析每一行的JSON数据
            item = json.loads(line)
            new_dict = {}
            new_dict['img_path'] = item['image']
            new_dict['input_desc'] = item['detail_caption'][0]

            final.append(new_dict)

with open(output_json, 'w', encoding='utf-8') as f:
    json.dump(final, f, indent=4, ensure_ascii=False)





