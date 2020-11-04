
from __future__ import absolute_import
import struct

def _pad_to(number_string, pad_length):
    """Pad a hexadecimal or binary string with leading zeros."""
    leader, number = number_string[:2], number_string[2:]
    return '{:2s}{:s}{:s}'.format(leader,
                                  '0' * (pad_length - len(number)),
                                  number)

def float_to_bin(f):
    """Convert a 32-bit float to binary."""
    try:
        bytes = struct.pack('<f', f)
        base10 = struct.unpack('<I', bytes)[0]
    except (TypeError, struct.error):
        raise ValueError('input cannot be converted to binary')
    return _pad_to(bin(base10), 32)


def bin_to_float(b):
    """Convert a 32-bit binary string to a 32-bit double."""
    try:
        base10 = int(b, 2)
        bytes = struct.pack('<I', base10)
    except (TypeError, struct.error):
        raise ValueError('input cannot be converted to float')
    return struct.unpack('<f', bytes)[0]

var_1 = float_to_bin(10.256)
print("binary---> ", var_1)
var_2 = bin_to_float('11001')
print("float---> ", var_2)

sign = False
input_value = str(100.25)
input_value = input_value.split(".")
part_a = input_value[0]
part_b = input_value[1]
if(part_a[0] == '-'):
    sign = True
    part_a = part_a.split("-")
    part_a = part_a[1]

binary_part_a = bin(int(part_a))

print(part_a)
print(part_b)

print(bin(625))

#####################################################

import numpy as np

x_old = np.array([[1.001, 2.123, 4.785], [3.034, 1.00134, 1.00235], [2.2, 1.0017, 3.034]], np.float32)
a, b = np.modf(x_old)
print(a)
print(b)

print(np.fabs(x_old))

new_val = np.trunc(x_old, where=True)
print("trunc--> ", new_val)
################################

input_arry= np.array([[-0.2126, -0.0051, -0.1178,  0.2002, -0.1357, -0.1981,  0.0927, -0.1823,
-0.0493, -0.1427,  0.0243,  0.1891,  0.2406, -0.0049, -0.1408,  0.0373], [-0.2171, -0.0120, -0.1089,  0.2102, -0.1634,
-0.1492,  0.1159, -0.1801, -0.0672, -0.1283,  0.0281,  0.1525,  0.2553, -0.0018, -0.1590,  0.0356], [-0.2017, -0.0082,
-0.1341,  0.1956, -0.1421, -0.1572,  0.1045, -0.1842, -0.0449, -0.1452,  0.0528,  0.1155,  0.2323, -0.0364,
-0.1579,  0.0336], [-0.2093, -0.0334, -0.1361,  0.2013, -0.1791, -0.1574,  0.1160, -0.1840, -0.0636, -0.1312,  0.0316,  0.1651,  0.2625, -0.0329, -0.1642,  0.0470]], np.float32)

print("input -->   ", input_arry)

#################################

x = np.round(input_arry, decimals=2)
print("decimal approx -->   ", x)
x_edit, count = np.unique(x, return_counts=True)
print("unique values -->   ", x_edit, count)

import torch
value = np.float(567)
value = torch.tensor(value, dtype=torch.float16)
print(value)

abc = torch.empty([2, 4])
print(abc)

