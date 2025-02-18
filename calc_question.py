#!/usr/bin/python3
a = [1/x for x in range(1, 101)]

csv_out = []

for val in a:
    csv_out.append(f'{val},{val.as_integer_ratio()[0]},{val.as_integer_ratio()[1]}\n')


with open('values.csv', 'w') as f:
    f.writelines(csv_out)