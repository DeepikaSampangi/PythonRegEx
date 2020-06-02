import re

input_para: str = '''
You are not who you think you are,
you are not what others think you are,
you are what you think others think of you
'''
key: str = "[y,Y]ou"
reg = re.compile(key)

subst_key: str = "we"
replaced_para: str = reg.sub(subst_key, input_para)

print(replaced_para)

# Replace new line with space
key1: str = "\n"
reg1 = re.compile(key1)

subst_key: str = " "
replaced_para: str = reg1.sub(subst_key, input_para)

print(replaced_para)