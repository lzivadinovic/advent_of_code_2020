from collections import Counter
# Counter returns dictionary like object where keys are hashable object
# and values are their count

def count_in_party(line):
    # we split it so we dont count it in list comperhansion
    num_in_party = len(line.split('\n'))
    count_dict = Counter(line.replace('\n',''))
    return len([ f for f in count_dict.values() if f == num_in_party ])


data = open('input6', 'r').read().split('\n\n')

print(sum([ count_in_party(line) for line in data ]))



