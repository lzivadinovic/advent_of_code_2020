import re

# just parse data nicely
data = open('input4', 'r').read().split('\n\n')
req_f = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
#r = map(lambda line: 1 if req_f.issubset(set(re.split(':| ',line.replace('\n', ' '))[::2])), data)
data = [ 1 for line in data if req_f.issubset(set(re.split(':| ',line.replace('\n', ' '))[::2]))]

print(len(data))
