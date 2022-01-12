'''
import re

data = b'\x11\x22\x33\x44\x55\x66\x77\x88'
data_str = str(data.hex())
pattern = re.compile('.{2}')

data_str = '-'.join(pattern.findall(data_str))

print(data_str)

'''

dict = {}
dict['1'] = '2'
dict['1'] = '3' 

for item in dict:
    print(dict[item])