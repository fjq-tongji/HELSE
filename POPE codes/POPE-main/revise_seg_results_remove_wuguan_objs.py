import json


yuan_lst = []
with open('./CODA2022_img_name_segmentation_result-yuan.json', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            # 解析每一行的JSON数据
            item = json.loads(line)
            yuan_lst.append(item)

traffic_components = ['person', 'bicycle', 'car', 'road', 'building', 'tree', 'house', 'light', 'train', 'motorcycle', 'bench', 'bus', 'dirt', 'snow', 'truck', 'traffic light', 'bridge', 'tree', 'rock', 'mountain', 'ceiling', 'fire hydrant', 'stop sign', 'parking meter', 'cat', 'dog', 'pavement']
final_lst = []
for k in yuan_lst:
    new_dict = {}
    filter_objs = []
    objs_yuan = k['objects']
    for j in objs_yuan:
        if j in traffic_components:
            filter_objs.append(j)

    new_dict['image'] = k['image']
    new_dict['objects'] = filter_objs
    final_lst.append(new_dict)


for ii in final_lst:
    if len(ii['objects']) < 3:
        print(ii['image'])


###################
with open('./CODA2022_img_name_segmentation_result-revise.json', 'w', encoding='utf-8') as f:
    for item in final_lst:
        json.dump(item, f, ensure_ascii=False)
        f.write('\n')


