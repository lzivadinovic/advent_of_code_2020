with open('input3', 'r') as f:
    lines = [ line.strip('\n') for line in f.readlines() ]

moves = [(1,1),(3,1),(5,1),(7,1),(1,2)]
result = 1
rowWidth = len(lines[0])
for right, down in moves:
    position, count = 0, 0
    for row in lines[::down]:
        if row[position] == "#":
            count += 1
        position = (position+right)%rowWidth
    result = result * count

print("Multiplied results are: {}".format(result))

