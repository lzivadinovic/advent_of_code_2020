with open('input5') as fp:
    data = max([ int(line[0:7].replace('F', '0').replace('B', '1'),2)*8
            + 
            int(line[-4:-1].replace('L', '0').replace('R', '1'),2)
            for line in fp.readlines() if line.strip('\n') ])

print(data)
