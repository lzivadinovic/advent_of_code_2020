import re

# just parse data nicely
data = open('input4', 'r').read().split('\n\n')
req_f = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
valid = sum([req_f.issubset(set(re.split(':| ',line.replace('\n', ' '))[::2])) for line in data ]) 

print(valid)
