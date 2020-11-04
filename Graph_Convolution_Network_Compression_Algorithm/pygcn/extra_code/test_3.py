import numpy as np

def extract_binary_code(value, identify_key, data_type):
    bin_form = bin(value)
    bin_strip = str(bin_form).lstrip("0b")
    if identify_key is None:
        final_bin_form = bin_strip
    else:
        final_bin_form = str(identify_key) + bin_strip

    final_bin_form = int(final_bin_form, 2)
    final_bin_form = data_type(final_bin_form)
    return final_bin_form

def max_num_bits(value):
    start = 0
    cal = pow(2, start)
    while value >= cal:
        start = start + 1
        cal = pow(2, start)

    if value == cal:
        return start
    else:
        return start + 1

var = 32
for i in range(0, var):
    i = np.int8(i)
    data_type = np.uint8
    iden_key = 0
    res = extract_binary_code(i, iden_key, data_type)
    #print(res)

print(max_num_bits(1024))

import torch
abcd = [[12, 13], [5, 6]]
abcd = torch.tensor(abcd, dtype=torch.float16)
print(abcd)
print(abcd.dtype)
chk =abcd.dtype
abc = np.array([[12, 13], [5, 6]])
print(abc)
print(abc.dtype)
tmp = abc.dtype
if torch.is_tensor(abc):
    print('yes')
else:
    print('no')