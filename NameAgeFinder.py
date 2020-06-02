import re

name_age_sentence : str = '''
Jack is of age 21 and Jill is of age 18
Tom is of age 8 and Jerry is of age 4
Groot is of age 1 and Rocket is of age 2
'''

ages :dict = re.findall(r'\d{1,3}', name_age_sentence)

names :dict = re.findall(r'[A-Z][a-z]*', name_age_sentence)

age_dict :dict = {}
x=0
for name in names:
    age_dict[name] = ages[x]
    x+=1

print(age_dict)