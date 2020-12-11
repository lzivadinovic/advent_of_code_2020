with open('input3', 'r') as f:
    lines = [ line.strip('\n') for line in f.readlines() ]

position, count = 0, 0
rowWidth = len(lines[0])

for row in lines:
    if row[position] == "#":
        count += 1
    position = (position+3)%rowWidth

print("Total number of trees (#) encountered is: {}".format(count))
