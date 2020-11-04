import torch
import numpy as np

torch_list = torch.tensor([10, 2, 3, 10, 7, 4, 7], dtype=torch.uint8)
dict_n = {}
compare_list = []
for val in torch_list:
    if len(compare_list) == 0:
        dict_n[val] = val
        compare_list.append(val)

    elif not (compare_list.count(val) == 1):
        dict_n[val] = val
        compare_list.append(val)

print(len(dict_n.values()))
