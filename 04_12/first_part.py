import re

# just parse data nicely
data = open('input4', 'r').read().split('\n\n')
data = [ line.replace('\n', ' ') for line in data ]

# Create set of required fields
req_f = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
# optional_f = 'cid'

# initialize counter
counter = 0
for line in data:
    # Ask if req_f is subset of keys in row
    # set1 is subset of set 2 if every element of set1 is in set2
    # This also means set1 is subset of set2 if they are equal
    # re.split(':| ') -> split if either ':' or ' '
    # List every second element -> list only keys
    if req_f.issubset(set(re.split(':| ', line)[::2])):
        counter += 1

print(counter)
