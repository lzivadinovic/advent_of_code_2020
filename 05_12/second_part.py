with open('input5') as fp:
    data = [ int(line[0:7].replace('F', '0').replace('B', '1'),2)*8
            + 
            int(line[-4:-1].replace('L', '0').replace('R', '1'),2)
            for line in fp.readlines() if line.strip('\n') ]
valmin = min(data)
valmax = max(data)
valsum = sum(data)

# sum of numbers up to valmax
# minus sum of values up to valmin - 1
suma = 0.5 * (valmax*(valmax+1) - valmin*(valmin-1))
    
print(suma-valsum)


###### OR ###

a = sorted(data)    
for num, el in enumerate(a):
    if a[num+1]-el != 1:
        print(el+1)
        break

