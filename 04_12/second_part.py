import re

# just parse data nicely
# use '\n\n' as newline
data = open('input4', 'r').read().split('\n\n')
# split in key value pairs but replace \n with ' ' because we split it with '\n\n'
data_list = [(re.split(':| ',line.replace('\n', ' '))) for line in data ]
# Create dicts so we can validate
list_of_dicts = [ dict(zip(array[::2], array[1::2])) for array in data_list ]


from validator import validate_many, validate

#Custom validator functions
def validate_hgt(hgt):
    if hgt:    
        if hgt[-2:] == 'cm':
            return True if 150 <= int(hgt[:-2]) <= 193 else False
        elif hgt[-2:] == 'in':
            return True if 59 <= int(hgt[:-2]) <= 76 else False
    else:
        #Required or is kind of buggy if combined with custom function 
        return False
    
def validate_ecl(ecl):
    return True if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] else False

# required and regexp is broken
def validate_hcl(hcl):
    regexp = re.compile('^#[a-fA-F0-9]{6}$')
    return True if hcl and regexp.match(hcl) else False

rules = { 'byr' : "required|integer|between:1920,2002",
             'iyr' : "required|integer|between:2010,2020",
             'eyr' : "required|integer|between:2020,2030",
             'hgt' : validate_hgt,
             'hcl' : validate_hcl, #"required|regex:^#[a-fA-F0-9]{6}$",
             'ecl' : validate_ecl, 
             'pid' : "required|string|size:9"
}

#a = validate_many(list_of_dicts,rules) # Just returns true or false, not count
counter = 0
for line in list_of_dicts:
    if validate(line, rules): #IDK why it prints "function" /shrug"
        counter+=1
print(counter)


