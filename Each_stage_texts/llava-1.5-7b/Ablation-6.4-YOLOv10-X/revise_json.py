import json

file_path_1 = './YOLOv10_x_results.json'
file_path_2 = './YOLOv10_x_results_gai.json'

with open(file_path_1, 'r', encoding='utf-8') as f:
    f_1 = json.load(f)

lst = []
for k in range(len(f_1)):
    new_dict = {}
    new_dict['img_path'] = f_1[k]['img_path'][:-1]
    new_dict['YOLOv10_x_results'] = f_1[k]['YOLOv10_x_results']
    lst.append(new_dict)

with open(file_path_2, 'w', encoding='utf-8') as f:
    json.dump(lst, f, indent=4, ensure_ascii=False)












