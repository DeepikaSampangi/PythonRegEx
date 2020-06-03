import re

# . matches any input other than a new line \n

input_str1: str = "abc.123.qwe.392"

pat1: str = "^...\....\....\....$"

if re.findall(pat1, input_str1):
    print(f"The input {input_str1} matches the pattern {pat1}")
else:
    print(f"The input {input_str1} doenst matche the pattern {pat1}")


# \D matches any charancter that is not a digit

input_str2: str = "12A92,1234$12a"

pat2:str = "[0-9]{2}\D[0-9]{2}\D[0-9]{4}\D[0-9]{2}\D"

if re.findall(pat2, input_str2):
    print(f"The input {input_str2} matches the pattern {pat2}")
else:
    print(f"The input {input_str2} doesnt match the pattern {pat2}")
