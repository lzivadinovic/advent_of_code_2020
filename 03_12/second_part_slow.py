with open('input3', 'r') as f:
    lines = [ line.strip('\n') for line in f.readlines() ]

moves = [(1,1),(3,1),(5,1),(7,1),(1,2)]
count = [0]*len(moves)
rowWidth = len(lines[0])
for itter, row in enumerate(lines):
    for itterMoves, data in enumerate(moves):
        if itter % data[1] == 0:
            position = int(data[0]*itter/data[1])%rowWidth
            if row[position] == "#":
                count[itterMoves] +=1

from functools import reduce
result = reduce(lambda x, y: x*y, count)
print("Multiplied results are: {}".format(result))

