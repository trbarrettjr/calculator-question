#!/usr/bin/python3
import math

a = [1/x for x in range(1, 101)]

csv_out = ['float,denominator,numerator,base2 denominator,base2 numerator\n']

for val in a:
    csv_out.append(f'{val},'\
                   f'{val.as_integer_ratio()[0]},'\
                   f'{val.as_integer_ratio()[1]},'\
                   f'{math.log2(val.as_integer_ratio()[0])},'\
                   f'{math.log2(val.as_integer_ratio()[1])}\n')


with open('values.csv', 'w') as f:
    f.writelines(csv_out)