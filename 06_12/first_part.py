data = open('input6', 'r').read().split('\n\n')

print(sum([ len(set(line.replace('\n',''))) for line in data  ]))

'''
sum([ len(set(line.replace('\n',''))) for line in open('input6', 'r').read().split('\n\n') ])
'''
